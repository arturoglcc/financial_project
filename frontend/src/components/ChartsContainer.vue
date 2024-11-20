<template>
  <div class="charts-container">
    <div class="chart-item">
      <div ref="chartRefLeft" class="chart"></div>
    </div>
    <div class="chart-item">
      <div ref="chartRefRight" class="chart"></div>
    </div>
    <div class="chart-item">
      <div ref="chartRefBottomLeft" class="chart"></div>
    </div>
    <div class="chart-item">
      <div ref="chartRefBottomRight" class="chart"></div>
    </div>


    <!-- New Pie Charts -->
    <div class="chart-item">
      <div ref="chartRefPieIncome" class="chart"></div>
    </div>
    <div class="chart-item">
      <div ref="chartRefPieExpense" class="chart"></div>
    </div>
  </div>


</template>

<script>
import { onMounted, ref } from 'vue';
import * as echarts from 'echarts';
import axios from 'axios';

export default {
  setup() {
    const chartRefLeft = ref(null);
    const chartRefRight = ref(null);
    const chartRefBottomLeft = ref(null);
    const chartRefBottomRight = ref(null);
    const chartRefPieIncome = ref(null);
    const chartRefPieExpense = ref(null);

    const generateRandomData = (points) => {
      return Array.from({ length: points }, () => Math.floor(Math.random() * 10000));
    };

    const initChart = (chartRef, chartData) => {
      const chartInstance = echarts.init(chartRef);
      chartInstance.setOption(chartData);
      window.addEventListener('resize', () => {
        chartInstance.resize();
        });
    };

    const initPieChart = (chartRef, title, data) => {
      const chartInstance = echarts.init(chartRef);
      const option = {
        title: { text: title, left: 'center' },
        tooltip: { trigger: 'item' },
        series: [
          {
            name: title,
            type: 'pie',
            radius: '50%',
            data,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
              },
            },
          },
        ],
      };
      chartInstance.setOption(option);
      window.addEventListener('resize', () => {
        chartInstance.resize();
      });
    };
    const fetchAndPreparePieChartData = async (url, chartRef, title) => {
      try {
        const response = await axios.get(url, {
          withCredentials: true, // Include cookies or authentication headers
        });
        const items = response.data;

        const tagCounts = items.reduce((acc, item) => {
          item.tags.forEach((tag) => {
            acc[tag] = (acc[tag] || 0) + 1;
          });
          return acc;
        }, {});

        const chartData = Object.entries(tagCounts).map(([name, value]) => ({
          name,
          value,
        }));

        initPieChart(chartRef, title, chartData);
     } catch (error) {
        console.error(`Error fetching data for ${title}:`, error);
        // Optional: Display a fallback chart or message
        initPieChart(chartRef, title, []);
      }
    };


    onMounted(() => {
      // Initialize line charts
      initChart(chartRefLeft.value, {
        title: { text: 'Movements per week' },
        legend: { left: 'center', data: ['Incomes', 'Outlays'] },
        xAxis: { type: 'category', data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] },
        yAxis: { type: 'value' },
        series: [
          {
            name: 'Incomes',
            type: 'line',
            data: generateRandomData(7),
            lineStyle: { color: 'rgba(75, 192, 192, 1)' }, 
            itemStyle: { color: 'rgba(75, 192, 192, 1)' }, 
          },
          {
            name: 'Outlays',
            type: 'line',
            data: generateRandomData(7),
            lineStyle: { color: '#E70707' }, 
            itemStyle: { color: '#E70707' },
          },
        ],
      });

      initChart(chartRefRight.value, {
        title: { text: 'Movements per fortnight' },
        legend: { left: '41%', data: ['Incomes', 'Outlays'] },
        xAxis: { type: 'category', data: Array.from({ length: 14 }, (_, i) => `Day ${i + 1}`) },
        yAxis: { type: 'value' },
        series: [
          {
            name: 'Incomes',
            type: 'line',
            data: generateRandomData(14),
            lineStyle: { color: 'rgba(75, 192, 192, 1)' },
            itemStyle: { color: 'rgba(75, 192, 192, 1)' },
          },
          {
            name: 'Outlays',
            type: 'line',
            data: generateRandomData(14),
            lineStyle: { color: '#E70707' },
            itemStyle: { color: '#E70707' },
          },
        ],
      });

      initChart(chartRefBottomLeft.value, {
        title: { text: 'Movements per month' },
        legend: { left: '37%', data: ['Incomes', 'Outlays'] },
        xAxis: { type: 'category', data: ['Week 1', 'Week 2', 'Week 3', 'Week 4'] },
        yAxis: { type: 'value' },
        series: [
          {
            name: 'Incomes',
            type: 'line',
            data: generateRandomData(4),
            lineStyle: { color: 'rgba(75, 192, 192, 1)' },
            itemStyle: { color: 'rgba(75, 192, 192, 1)' },
          },
          {
            name: 'Outlays',
            type: 'line',
            data: generateRandomData(4),
            lineStyle: { color: '#E70707' },
            itemStyle: { color: '#E70707' },
          },
        ],
      });

      initChart(chartRefBottomRight.value, {
        title: { text: 'Movements per year' },
        legend: { left: 'center', data: ['Incomes', 'Outlays'] },
        xAxis: { type: 'category', data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] },
        yAxis: { type: 'value' },
        series: [
          {
            name: 'Incomes',
            type: 'line',
            data: generateRandomData(12),
            lineStyle: { color: 'rgba(75, 192, 192, 1)' },
            itemStyle: { color: 'rgba(75, 192, 192, 1)' },
          },
          {
            name: 'Outlays',
            type: 'line',
            data: generateRandomData(12),
            lineStyle: { color: '#E70707' },
            itemStyle: { color: '#E70707' },
          },
        ],
      });

      // Initialize pie charts
      fetchAndPreparePieChartData('http://localhost/api/allIncomes', chartRefPieIncome.value, 'Income Tags Distribution');
      fetchAndPreparePieChartData('http://localhost/api/allExpenses', chartRefPieExpense.value, 'Expense Tags Distribution');
    });

    return { chartRefLeft, chartRefRight, chartRefBottomLeft, chartRefBottomRight, chartRefPieIncome, chartRefPieExpense };
  },
};
</script>

<style scoped>
.charts-container {
  margin-top: 20px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(2, 1fr);
  gap: 20px;
  margin-bottom: 20px;
}

.chart-item {
  background-color: #fff;
  border-radius: 10px;
  border: 1px solid #ccc;
  padding: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.chart {
  height: 400px;
}
</style>