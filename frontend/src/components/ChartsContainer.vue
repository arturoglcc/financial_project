<template>
  <div class="charts-container">
    <div class="chart-item">
      <WeekChart class="chart" />
    </div>
    <div class="chart-item">
      <FortnightChart class="chart" />
    </div>
    <div class="chart-item">
      <MonthChart class="chart" />
    </div>
    <div class="chart-item">
      <YearChart class="chart" />
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
import WeekChart from './WeekChart.vue';
import FortnightChart from './FortnightChart.vue';
import MonthChart from './MonthChart.vue';
import YearChart from './YearChart.vue';

export default {
  components: {
    WeekChart,
    FortnightChart,
    MonthChart,
    YearChart,
  },
  setup() {
    const chartRefPieIncome = ref(null);
    const chartRefPieExpense = ref(null);

    const initChart = (chartRef, chartData) => {
      const chartInstance = echarts.init(chartRef);

      const option = {
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

    // Create the chart data from the backend response
    const chartData = items.map(item => ({
      name: item.tag,
      value: item.total,
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
  // Initialize pie charts with new endpoints
  fetchAndPreparePieChartData('http://localhost/api/incomesTags', chartRefPieIncome.value, 'Income Tags Distribution');
  fetchAndPreparePieChartData('http://localhost/api/expensesTags', chartRefPieExpense.value, 'Expense Tags Distribution');
});


    return { chartRefPieIncome, chartRefPieExpense };
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