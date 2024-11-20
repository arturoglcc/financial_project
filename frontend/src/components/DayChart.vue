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
      const data = ref({ incomes: Array(24).fill(0), outlays: Array(24).fill(0) });

      const fetchTransactions = async () => {
        try {

          // Start date: midnight of one day ago
          const start_date = new Date();
          start_date.setDate(start_date.getDate() - 1); // One day ago

          // End date: midnight of today
          const end_date = new Date();
          end_date.setDate(start_date.getDate() + 1)


          // Helper function to construct the URL with query parameters
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

         // Process transactions to map amounts to hours
        const processTransactions = (transactions) => {
          const result = Array(24).fill(0); // Initialize an array for 24 hours
          transactions.forEach((transaction) => {
            const date = new Date(transaction.date_time);
            const hour = date.getHours(); // Extract the hour
            result[hour] += parseFloat(transaction.amount); // Add the amount to the correct hour
          });
          return result;
        };

        // Fetch both incomes and outlays
        const [incomes, outlays] = await Promise.all([fetchIncomes(), fetchOutlays()]);
        data.value = {
          incomes: processTransactions(incomes),
          outlays: processTransactions(outlays),
        };
      } catch (error) {
          console.error('Error fetching transactions:', error);
          data.value = { incomes: Array(24).fill(0), outlays: Array(24).fill(0) }; // Default fallback
        }
      };

    const initChart = () => {
      if (!data) {
        console.error('Chart initialization error: data is undefined.');
        return;
      }
      const chartInstance = echarts.init(chartRef.value);

      // Generate labels for the last 24 hours
      const generateLabels = () => {
        const labels = [];
        const now = new Date();
        for (let i = 23; i >= 0; i--) {
          const date = new Date(now);
          date.setHours(now.getHours() - i);
          const label = `${date.getHours()}:00`;
          labels.push(label);
        }
        return labels;
      };

      const option = {
        color: ['rgba(75, 192, 192, 1)', '#E70707'],
        title: {
          text: 'Movements per day',
        },
        tooltip: {
          trigger: 'axis',
        },
        legend: {
          data: ['Incomes', 'Outlays'],
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        xAxis: {
          type: 'category',
          data: generateLabels(),
          axisPointer: { type: 'shadow' },
          name: 'Hours',
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
            padding: 30,
          },
        },
        series: [
          {
            name: 'Incomes',
            type: 'line',
            data: data.value.incomes,
          },
          {
            name: 'Outlays',
            type: 'line',
            data: data.value.outlays,
          }
        ],
        grid: {
          left: '5%',
          right: '5%',
          top: '10%',
          bottom: '10%',
        },
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