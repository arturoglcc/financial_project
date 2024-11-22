<template>
  <div class="chart-container">
    <div ref="chartRef" class="chart"></div>
  </div>
</template>

<script>
  import { onMounted, ref } from 'vue';
  import * as echarts from 'echarts';

  export default {
    setup() {
      const chartRef = ref(null);
      const data = ref({ incomes: Array(15).fill(0), outlays: Array(15).fill(0) });

      const fetchTransactions = async () => {
        try {
          const start_date = new Date();
          start_date.setDate(start_date.getDate() - 15); 
          start_date.setHours(0, 0, 0, 0);

          const end_date = new Date();

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
            const result = Array(15).fill(0);
            transactions.forEach((transaction) => {
              const date = new Date(transaction.date_time);
              const dayIndex = Math.floor((date - start_date) / (1000 * 60 * 60 * 24));
              if (dayIndex >= 0 && dayIndex < 15) {
                result[dayIndex] += parseFloat(transaction.amount);
              }
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

        const labels = Array.from({ length: 15 }, (_, i) => {
          const date = new Date();
          date.setDate(date.getDate() - 14 + i);
          return `${date.getDate()} ${date.toLocaleString('default', { month: 'short' })}`;
        });

        const option = {
          title: { text: 'Movements per Fortnight' },
          xAxis: {
            type: 'category',
            data: labels,
            axisPointer: { type: 'shadow' },
          },
          yAxis: {
            type: 'value',
            name: 'Amount $',
          },
          series: [
            { name: 'Incomes', type: 'line', data: data.value.incomes },
            { name: 'Outlays', type: 'line', data: data.value.outlays },
          ],
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

<style scoped>
.chart-container {
  display: flex;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.chart {
  flex: 1;
  height: 400px;
}
</style>