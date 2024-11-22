<template>
  <div ref="chartRef"></div>
</template>

<script>
import { onMounted, ref } from 'vue';
import * as echarts from 'echarts';

export default {
  setup() {
    const chartRef = ref(null);
    const data = ref({ incomes: Array(7).fill(0), outlays: Array(7).fill(0) });

    const fetchTransactions = async () => {
      const start_date = new Date();
      start_date.setDate(start_date.getDate() - 7); // Start from 7 days ago
      start_date.setHours(0, 0, 0, 0);

      const end_date = new Date(); // Current date and time

      // Helper function to construct the URL with query parameters
      function buildUrl(baseUrl, params) {
        const url = new URL(baseUrl);
        Object.keys(params).forEach((key) => {
          url.searchParams.append(key, params[key]);
        });
        return url.toString();
      }

      let incomes = [];
      let outlays = [];

      // Fetch incomes
      try {
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

        const incomesData = await incomesResponse.json();
        incomes = incomesData.map((transaction) => ({
          date: new Date(transaction.date_time),
          amount: parseFloat(transaction.amount),
        }));
      } catch (error) {
        console.error('Error fetching incomes:', error);
      }

      // Fetch outlays
      try {
        const outlaysUrl = buildUrl('http://localhost/api/transactions', {
          start_date: start_date.toISOString(),
          end_date: end_date.toISOString(),
          transaction_type: 'expense',
        });

        const outlaysResponse = await fetch(outlaysUrl, {
          method: 'GET',
          headers: { Accept: 'application/json' },
          credentials: 'include', // Include credentials if required
        });

        if (!outlaysResponse.ok) {
          throw new Error(`Error fetching outlays: ${outlaysResponse.statusText}`);
        }

        const outlaysData = await outlaysResponse.json();
        outlays = outlaysData.map((transaction) => ({
          date: new Date(transaction.date_time),
          amount: parseFloat(transaction.amount),
        }));
      } catch (error) {
        console.error('Error fetching outlays:', error);
      }

      // Process transactions to aggregate amounts by day of the week
      const processTransactions = (transactions) => {
        const result = Array(7).fill(0); // Initialize an array for 7 days
        transactions.forEach((transaction) => {
          const dayIndex = (transaction.date.getDay() + 6) % 7; // Adjust to start week on Monday
          result[dayIndex] += transaction.amount;
        });
        return result;
      };

      // Update data, ensuring fallback values if one type is missing
      data.value = {
        incomes: incomes.length ? processTransactions(incomes) : Array(7).fill(0),
        outlays: outlays.length ? processTransactions(outlays) : Array(7).fill(0),
      };
    };

    const initChart = () => {
      const chartInstance = echarts.init(chartRef.value);

      const option = {
        color: ['rgba(75, 192, 192, 1)', '#E70707'],
        title: { text: 'Movements per Week' },
        tooltip: {
          trigger: 'axis',
          valueFormatter: (value) => '$ ' + value,
        },
        legend: { data: ['Incomes', 'Outlays'], icon: 'circle' },
        toolbox: {
          feature: { magicType: { type: ['line', 'bar'] }, restore: {}, saveAsImage: {} },
        },
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
          axisPointer: { type: 'shadow' },
          name: 'Days',
          nameLocation: 'center',
          nameTextStyle: {
            fontStyle: 'italic',
            fontWeight: 'bold',
            fontSize: 15,
            padding: 10,
          },
        },
        yAxis: {
          type: 'value',
          name: 'Amount $',
          nameLocation: 'center',
          nameTextStyle: {
            fontStyle: 'italic',
            fontWeight: 'bold',
            fontSize: 15,
            padding: 40,
          },
          axisLabel: { formatter: '$ {value}' },
        },
        series: [
          {
            name: 'Incomes',
            type: 'line',
            emphasis: { focus: 'series' },
            data: data.value.incomes,
          },
          {
            name: 'Outlays',
            type: 'line',
            emphasis: { focus: 'series' },
            data: data.value.outlays,
          },
        ],
        grid: { left: '12%', right: '5%', top: '10%', bottom: '10%' },
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
