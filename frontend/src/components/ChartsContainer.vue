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

      let option;
      if (chartData.type == 'pie') {
        option = {
          title: { text: chartData.title, left: 'center', },
          tooltip: { trigger: 'item', formatter: '{a} <br/>{b}: {c} ({d}%)', },
          legend: { orient: 'vertical', left: 'left', },
          toolbox: { feature: { saveAsImage: {} } },
          series: [
            {
              name: chartData.seriesName,
              type: 'pie',
              radius: '50%',
              data: chartData.seriesData,
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
      } else {
        option = {
          color: ['rgba(75, 192, 192, 1)', '#E70707'],
          title: { text: chartData.title, },
          tooltip: { trigger: 'axis', valueFormatter: (value) => '$ ' + value, },
          legend: { data: ['Incomes', 'Outlays'], left: chartData.legendLeft, icon: 'circle', },
          toolbox: { feature: { magicType: { type: ['line', 'bar'] }, restore: {}, saveAsImage: {} } },
          xAxis: {
            type: 'category',
            data: chartData.xAxisData,
            axisPointer: { type: 'shadow' },
            name: chartData.xAxisName,
            nameLocation: 'center',
            nameTextStyle: { fontStyle: 'italic', fontWeight: 'bold', fontSize: 15, padding: 10, },
          },
          yAxis: {
            type: 'value',
            name: 'Amount $',
            nameLocation: 'center',
            nameTextStyle: { fontStyle: 'italic', fontWeight: 'bold', fontSize: 15, padding: 40, },
            axisLabel: { formatter: '$ {value}', }
          },
          series: [
            {
              name: 'Incomes',
              type: 'line',
              emphasis: { focus: 'series' },
              data: chartData.yAxisDataIncome,
            },
            {
              name: 'Outlays',
              type: 'line',
              emphasis: { focus: 'series' },
              data: chartData.yAxisDataOutlay,
            }
          ],
          grid: { left: '12%', right: '5%', top: '10%', bottom: '10%', },
        };
      }

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

        initChart(chartRef, {
          type: 'pie',
          title,
          seriesName: title,
          seriesData: chartData,
        });
      } catch (error) {
        console.error(`Error fetching data for ${title}:`, error);
        // Optional: Display a fallback chart or message
        initChart(chartRef, {
          type: 'pie',
          title,
          seriesName: title,
          seriesData: [],
        });
      }
    };

    onMounted(() => {
      // Initialize line charts
      initChart(chartRefLeft.value, {
        title: 'Movements per week',
        legendLeft: 'center',
        xAxisData: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        yAxisDataIncome: generateRandomData(7),
        yAxisDataOutlay: generateRandomData(7),
        xAxisName: 'Days',
      });

      initChart(chartRefRight.value, {
        title: 'Movements per fortnight',
        legendLeft: '41%',
        xAxisData: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        yAxisDataIncome: generateRandomData(14),
        yAxisDataOutlay: generateRandomData(14),
        xAxisName: 'Days',
      });

      initChart(chartRefBottomLeft.value, {
        title: 'Movements per month',
        legendLeft: '37%',
        xAxisData: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        yAxisDataIncome: generateRandomData(4),
        yAxisDataOutlay: generateRandomData(4),
        xAxisName: 'Weeks',
      });

      initChart(chartRefBottomRight.value, {
        title: 'Movements per year',
        legendLeft: 'center',
        xAxisData: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        yAxisDataIncome: generateRandomData(12),
        yAxisDataOutlay: generateRandomData(12),
        xAxisName: 'Months',
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