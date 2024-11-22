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
      // Start date: midnight of one day ago
      const start_date = new Date();
      start_date.setHours(0, 0, 0, 0);

      // End date: midnight of today
      const end_date = new Date(start_date);
      end_date.setDate(end_date.getDate() + 1); // Move to the next day
      end_date.setHours(0, 0, 0, 0);

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
          hour: new Date(transaction.date_time).getHours(),
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
          headers: {
            Accept: 'application/json',
          },
          credentials: 'include', // Include credentials if required
        });

        if (!outlaysResponse.ok) {
          throw new Error(`Error fetching outlays: ${outlaysResponse.statusText}`);
        }

        const outlaysData = await outlaysResponse.json();
        outlays = outlaysData.map((transaction) => ({
          hour: new Date(transaction.date_time).getHours(),
          amount: parseFloat(transaction.amount),
        }));
      } catch (error) {
        console.error('Error fetching outlays:', error);
      }

      // Process data into a format suitable for the chart
      const processTransactions = (transactions) => {
        const result = Array(24).fill(0); // Initialize an array for 24 hours
        transactions.forEach((transaction) => {
          result[transaction.hour] += transaction.amount;
        });
        return result;
      };

      // Update data
      data.value = {
        incomes: processTransactions(incomes),
        outlays: processTransactions(outlays),
      };
    };

    const initChart = () => {
      if (!chartRef.value) {
        console.error('Chart initialization error: chartRef is undefined.');
        return;
      }

      const chartInstance = echarts.init(chartRef.value);

      // Generate labels for the last 24 hours
      const generateLabels = () => {
        const labels = [];
        for (let i = 0; i < 24; i++) {
          labels.push(`${i}:00`); // Label each hour (0:00 to 23:00)
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
          valueFormatter: (value) => '$ ' + value,
        },
        legend: {
          data: ['Incomes', 'Outlays'],
          icon: 'circle',
        },
        toolbox: {
          feature: {
            magicType: { type: ['line', 'bar'] },
            restore: {},
            saveAsImage: {},
          },
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
            padding: 40,
          },
          axisLabel: {
            formatter: '$ {value}',
          },
        },
        series: [
          {
            name: 'Incomes',
            type: 'line',
            emphasis: {
              focus: 'series',
            },
            data: data.value.incomes.length ? data.value.incomes : Array(24).fill(0),
          },
          {
            name: 'Outlays',
            type: 'line',
            emphasis: {
              focus: 'series',
            },
            data: data.value.outlays.length ? data.value.outlays : Array(24).fill(0),
          },
        ],
        grid: {
          left: '6%',
          right: '2.5%',
          top: '10%',
          bottom: '10%',
        },
      };

      chartInstance.setOption(option);

      // Handle window resize to make the chart responsive
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