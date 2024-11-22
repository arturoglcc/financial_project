<template>
  <div ref="chartRef"></div>
</template>

<script>
import { onMounted, ref } from 'vue';
import * as echarts from 'echarts';

export default {
  setup() {
    const chartRef = ref(null);
    const data = ref({ incomes: Array(31).fill(0), outlays: Array(31).fill(0) });

    const fetchTransactions = async () => {
      try {
        const start_date = new Date();
        start_date.setDate(1);
        start_date.setHours(0, 0, 0, 0);

        const end_date = new Date();
        end_date.setMonth(end_date.getMonth() + 1, 1);
        end_date.setHours(0, 0, 0, 0);

        // Helper functions y lógica para fetch (igual que en DayChart.vue)
        function buildUrl(baseUrl, params) {
          const url = new URL(baseUrl);
          Object.keys(params).forEach(key => {
            url.searchParams.append(key, params[key]);
          });
          return url.toString();
        }

        // Fetch incomes
        const fetchIncomes = async () => {
          const incomesUrl = buildUrl('http://localhost/api/transactions', {
            start_date: start_date.toISOString(),
            end_date: end_date.toISOString(),
            transaction_type: 'income',
          });

          const incomesResponse = await fetch(incomesUrl, {
            method: 'GET',
            credentials: 'include', // Include credentials if required
          });

          if (!incomesResponse.ok) {
            throw new Error(`Error fetching incomes: ${incomesResponse.statusText}`);
          }

          return incomesResponse.json();
        };

        // Fetch outlays
        const fetchOutlays = async () => {
          const outlaysUrl = buildUrl('http://localhost/api/transactions', {
            start_date: start_date.toISOString(),
            end_date: end_date.toISOString(),
            transaction_type: 'expense',
          });

          const outlaysResponse = await fetch(outlaysUrl, {
            method: 'GET',
            headers: {
              'Accept': 'application/json',
            },
            credentials: 'include', // Include credentials if required
          });

          if (!outlaysResponse.ok) {
            throw new Error(`Error fetching outlays: ${outlaysResponse.statusText}`);
          }

          return outlaysResponse.json();
        };

        const processTransactions = (transactions) => {
          const result = Array(31).fill(0);
          transactions.forEach((transaction) => {
            const date = new Date(transaction.date_time);
            const day = date.getDate() - 1;
            result[day] += parseFloat(transaction.amount);
          });
          return result;
        };

        const [incomes, outlays] = await Promise.all([fetchIncomes(), fetchOutlays()]);
        data.value = {
          incomes: processTransactions(incomes),
          outlays: processTransactions(outlays),
        };
      } catch (error) {
        console.error('Error fetching transactions:', error);
      }
    };

    const initChart = () => {
      const chartInstance = echarts.init(chartRef.value);

      const labels = Array.from({ length: 31 }, (_, i) => (i + 1).toString());

      const option = {
        color: ['rgba(75, 192, 192, 1)', '#E70707'],
        title: { text: 'Movements per Month' },
        tooltip: { trigger: 'axis', valueFormatter: (value) => '$ ' + value, },
        legend: { data: ['Incomes', 'Outlays'], left: '37%', icon: 'circle', },
        toolbox: { feature: { magicType: { type: ['line', 'bar'] }, restore: {}, saveAsImage: {} } },
        xAxis: {
          type: 'category',
          data: labels,
          axisPointer: { type: 'shadow' },
          name: 'Days',
          nameLocation: 'center',
          nameTextStyle: { fontStyle: 'italic', fontWeight: 'bold', fontSize: 15, padding: 10, },
        },
        yAxis: {
          type: 'value',
          name: 'Amount $',
          nameLocation: 'center',
          nameTextStyle: { fontStyle: 'italic', fontWeight: 'bold', fontSize: 15, padding: 40, },
          axisLabel: { formatter: '$ {value}', },
        },
        series: [
          {
            name: 'Incomes',
            type: 'line',
            emphasis: { focus: 'series' },
            data: data.value.incomes
          },
          {
            name: 'Outlays',
            type: 'line',
            emphasis: { focus: 'series' },
            data: data.value.outlays
          },
        ],
        grid: { left: '12%', right: '5%', top: '10%', bottom: '10%', },
      };

      chartInstance.setOption(option);
      window.addEventListener('resize', () => {
        chartInstance.resize();
      });
    };

    onMounted(async () => {
      await fetchTransactions();
      initChart();
    });

    return { chartRef };
  },
};
</script>
