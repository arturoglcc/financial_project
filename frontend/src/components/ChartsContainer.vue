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

    // Predefined bright colors
    const brightColors = [
      '#e74c3c', // Red
      '#3498db', // Light Blue
      '#2ecc71', // Green
      '#1abc9c', // Cyan
      '#f1c40f', // Yellow
      '#f39c12', // Orange
      '#9b59b6', // Light Purple
      '#ecf0f1', // White
    ];

    const tagColors = {}; // Store colors assigned to each tag

    // Function to assign colors to tags dynamically
    const generateDynamicColor = (index) => {
      const hue = (index * 137.508) % 360; // Golden angle increment
      return `hsl(${hue}, 70%, 60%)`;
    };

    const assignColor = (tag, index) => {
      if (!tagColors[tag]) {
        if (index < brightColors.length) {
          tagColors[tag] = brightColors[index];
        } else {
          tagColors[tag] = generateDynamicColor(index);
        }
      }
      return tagColors[tag];
    };

    // Function to blend colors of overlapping tags
    const blendColors = (tags) => {
      const rgbValues = tags.map((tag) =>
        (tagColors[tag] || '#000000')
          .slice(1) // Remove `#`
          .match(/.{1,2}/g) // Split into R, G, B
          .map((x) => parseInt(x, 16)) // Convert hex to decimal
      );

      const blended = rgbValues[0].map((_, i) =>
        Math.round(
          rgbValues.reduce((sum, rgb) => sum + rgb[i], 0) / rgbValues.length
        )
      );

      return `rgb(${blended.join(',')})`;
    };

    // Function to initialize overlapping pie chart
    const initOverlappingChart = (chartRef, chartData, title) => {
      if (!Array.isArray(chartData)) {
        console.error('chartData must be an array:', chartData);
        return;
      }

      if (!chartData.length) {
        const chartInstance = echarts.init(chartRef);
        chartInstance.setOption({
          title: {
            text: 'No Data Available',
            left: 'center',
          },
          series: [],
        });
        return;
      }

      const chartInstance = echarts.init(chartRef);

      const seriesData = chartData
        .map((item) => {
          const baseData = [
            {
              name: item.name,
              value: item.value,
              itemStyle: { color: assignColor(item.name, 0) }, // Assign tag color
            },
          ];

          const overlapData = item.overlaps.map((overlap) => ({
            name: overlap.name,
            value: overlap.value,
            itemStyle: { color: blendColors(overlap.tags) }, // Blend overlapping colors
          }));

          return [...baseData, ...overlapData];
        })
        .flat();

      const option = {
        title: {
          text: title,
          left: 'center',
        },
        tooltip: {
          trigger: 'item',
          formatter: '{b}: {c} ({d}%)',
        },
        series: [
          {
            name: title,
            type: 'pie',
            radius: ['40%', '70%'],
            data: seriesData,
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

    // Fetch data and prepare for the pie chart
    const fetchAndPreparePieChartData = async (url, chartRef, title) => {
      try {
        const response = await axios.get(url, { withCredentials: true });
        const items = response.data;

        if (!Array.isArray(items)) {
          throw new Error('API did not return an array');
        }

        const seenOverlaps = new Set();

        const chartData = items.map((item, index) => {
          const overlaps = (item.connections || [])
            .map((connectedTag) => {
              const sortedTags = [item.tag, connectedTag].sort();
              const overlapKey = sortedTags.join(' & ');

              if (!seenOverlaps.has(overlapKey)) {
                seenOverlaps.add(overlapKey);

                const connectedItem = items.find((i) => i.tag === connectedTag);
                const overlapValue = Math.min(
                  item.total,
                  connectedItem ? connectedItem.total : 0
                );

                return {
                  name: overlapKey,
                  value: overlapValue,
                  tags: sortedTags,
                  itemStyle: { color: blendColors(sortedTags) },
                };
              }

              return null; // Skip duplicate overlaps
            })
            .filter(Boolean);

          return {
            name: item.tag,
            value: item.total,
            overlaps,
            itemStyle: { color: assignColor(item.tag, index) },
          };
        });

        initOverlappingChart(chartRef, chartData, title);
      } catch (error) {
        console.error(`Error fetching data for ${title}:`, error);
        initOverlappingChart(chartRef, [], title);
      }
    };

    onMounted(() => {
      fetchAndPreparePieChartData(
        'http://localhost/api/incomesTags',
        chartRefPieIncome.value,
        'Income Tags Distribution'
      );
      fetchAndPreparePieChartData(
        'http://localhost/api/expensesTags',
        chartRefPieExpense.value,
        'Expense Tags Distribution'
      );
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