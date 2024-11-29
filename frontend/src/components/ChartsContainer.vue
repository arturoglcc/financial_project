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

    // Predefined colors
    const brightColors = [
      '#e74c3c', // Red
      '#3498db', // Light Blue
      '#2ecc71', // Green
      '#FF99CC', // pink
      '#f1c40f', // Yellow
      '#f39c12', // Orange
      '#9b59b6', // Light Purple
      '#ecf0f1', // White
    ];

    const tagColors = {}; // Store colors assigned to each tag

    const assignColor = (tags, index) => {
    // Loop through each tag and assign color if not already assigned
    tags.forEach((tag) => {
      if (!tagColors[tag]) {
        // Check if there's a pre-defined color from brightColors or generate one
        if (index < brightColors.length) {
          tagColors[tag] = brightColors[index];
        } else {
          tagColors[tag] = generateDynamicColor(index);
        }
        index++;
      }
    });
    if (tags.length > 1) {
    return blendColors(tags);
  }

    // Return the color for the first tag (or any logic you need)
    return tagColors[tags[0]]; // Return the color of the first tag or the last assigned color
};


    // Helper function to generate dynamic colors
    const generateDynamicColor = (index) => {
      const hue = (index * 137.508) % 360; // HSL color generation
      return `hsl(${hue}, 70%, 60%)`;
    };

    // Helper function to blend colors for overlapping tags
    const blendColors = (tags) => {
      const rgbValues = tags.map((tag) => {
        const color = tagColors[tag] || generateDynamicColor(Object.keys(tagColors).length);
        return color.slice(1).match(/.{1,2}/g).map((x) => parseInt(x, 16));
      });

      const blended = rgbValues[0].map((_, i) =>
        Math.round(
          rgbValues.reduce((sum, rgb) => sum + rgb[i], 0) / rgbValues.length
        )
      );

      return `rgb(${blended.join(',')})`;
    };

    // Function to initialize overlapping chart
    const initOverlappingChart = (chartRef, chartData, title) => {
      if (!chartRef) {
        console.error("Chart reference is not defined.");
        return;
      }

      // Dispose of existing chart instance
      const existingInstance = echarts.getInstanceByDom(chartRef);
      if (existingInstance) {
        echarts.dispose(chartRef);
      }

      // Initialize a new chart instance
      const chartInstance = echarts.init(chartRef);

      // Handle empty data gracefully
      if (!chartData || !chartData.length) {
        chartInstance.setOption({
          title: { text: "No Data Available", left: "center" },
          series: [],
        });
        return;
      }

      // Define chart options
      const option = {
        title: { text: title, left: "center" },
        tooltip: { trigger: "item", formatter: "{b}: {c} ({d}%)" },
        series: [
          {
            name: title,
            type: "pie",
            radius: ["40%", "70%"],
            data: chartData, // Directly use the provided chartData
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      };

      // Set chart options
      chartInstance.setOption(option);

      // Ensure the chart resizes dynamically
      window.addEventListener("resize", () => {
        chartInstance.resize();
      });
    };

    // Function to fetch and prepare pie chart data
    const fetchAndPreparePieChartData = async (url, chartRef, title) => {
      try {
        const response = await axios.get(url, { withCredentials: true });
        const items = response.data;

        const seenEntries = new Set(); // Track unique names
        const chartData = [];
        const tagTotals = {}; // Store totals for individual tags

        // Process combined tags
        Object.entries(items).forEach(([tags, value], loopIndex) => {
          const tagGroup = tags.split(",").map((tag) => tag.trim());
          const sortedTags = tagGroup.sort();
          const overlapKey = sortedTags.join(" & ");

          const combinedIndex = chartData.length + loopIndex + tagGroup.length - 1;
          const color = assignColor(sortedTags, combinedIndex);
          // Add combined tags only if unique
          if (!seenEntries.has(overlapKey)) {
            seenEntries.add(overlapKey);
            chartData.push({
              name: overlapKey,
              value,
              tags: sortedTags,
              itemStyle: { color: color},
            });
          }

          // Accumulate totals for individual tags
          tagGroup.forEach((tag) => {
            tagTotals[tag] = (tagTotals[tag] || 0) + value;
          });
        });

        // Pass the prepared chartData directly to the chart initializer
        initOverlappingChart(chartRef, chartData, title);
      } catch (error) {
        console.error(`Error fetching data for ${title}:`, error);
        initOverlappingChart(chartRef, [], title); // Initialize chart with empty data in case of error
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