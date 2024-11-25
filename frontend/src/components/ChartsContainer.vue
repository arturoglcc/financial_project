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

const assignColor = (tag, index) => {
  if (!tagColors[tag]) {
    if (index < brightColors.length) {
      tagColors[tag] = brightColors[index];
    } else {
      tagColors[tag] = generateDynamicColor(index);
    }
    console.log(`Assigned color for ${tag}: ${tagColors[tag]}`);
  }
  return tagColors[tag];
};

const generateDynamicColor = (index) => {
  const hue = (index * 137.508) % 360; // Golden angle increment
  return `hsl(${hue}, 70%, 60%)`;
};


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




const initOverlappingChart = (chartRef, chartData, title) => {
  if (!chartRef) {
    console.error("Chart reference is not defined.");
    return;
  }

  if (!Array.isArray(chartData)) {
    console.error("chartData must be an array:", chartData);
    return;
  }

  if (!chartData.length) {
    // Dispose of existing chart instance if any
    if (echarts.getInstanceByDom(chartRef)) {
      echarts.dispose(chartRef);
    }

    const chartInstance = echarts.init(chartRef);
    chartInstance.setOption({
      title: {
        text: "No Data Available",
        left: "center",
      },
      series: [],
    });
    return;
  }

  // Dispose of existing chart instance on the same DOM element
  if (echarts.getInstanceByDom(chartRef)) {
    echarts.dispose(chartRef);
  }

  // Initialize a new chart instance
  const chartInstance = echarts.init(chartRef);

  // Track unique names to ensure proper color assignment
  const uniqueNames = [...new Set(chartData.map((item) => item.name))];
  const nameIndexMap = uniqueNames.reduce((map, name, index) => {
    map[name] = index;
    return map;
  }, {});

  // Process the chart data to include base and overlap data
  const seriesData = chartData
    .map((item) => {
      const baseData = [
        {
          name: item.name,
          value: item.value,
          itemStyle: { color: assignColor(item.name, nameIndexMap[item.name]) }, // Assign unique color
        },
      ];

      const overlapData = (item.overlaps || []).map((overlap) => ({
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
      left: "center",
    },
    tooltip: {
      trigger: "item",
      formatter: "{b}: {c} ({d}%)",
    },
    series: [
      {
        name: title,
        type: "pie",
        radius: ["40%", "70%"],
        data: seriesData, // Use the processed series data
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

  // Set the chart options
  chartInstance.setOption(option);

  // Ensure the chart resizes when the window resizes
  window.addEventListener("resize", () => {
    chartInstance.resize();
  });
};




const fetchAndPreparePieChartData = async (url, chartRef, title) => {
  try {
    const response = await axios.get(url, { withCredentials: true });
    const items = response.data;

    if (typeof items !== 'object') {
      throw new Error('API did not return a valid object');
    }

    const seenCombinations = new Set();
    const chartData = [];
    const tagTotals = {}; // Store totals for individual tags

    // Process each key-value pair in the JSON
    Object.entries(items).forEach(([tags, value]) => {
      const tagGroup = tags.split(',').map((tag) => tag.trim()); // Split tags by `,` and trim spaces
      const sortedTags = tagGroup.sort(); // Sort to ensure unique combinations
      const overlapKey = sortedTags.join(' & ');

      // Accumulate totals for individual tags
      tagGroup.forEach((tag) => {
        if (!tagTotals[tag]) {
          tagTotals[tag] = 0;
        }
        tagTotals[tag] += value; // Add to total for this tag
      });

      // Add overlap entry if not already added
      if (!seenCombinations.has(overlapKey)) {
        seenCombinations.add(overlapKey);
        chartData.push({
          name: overlapKey, // Combined tags as a name
          value, // Directly use the value from the JSON
          tags: sortedTags,
          itemStyle: { color: blendColors(sortedTags) }, // Blend colors for overlap
        });
      }
    });

    // Add individual tags, subtracting overlapping values
    Object.entries(tagTotals).forEach(([tag, total], index) => {
      const nonOverlappingValue = total - chartData
        .filter((item) => item.tags?.includes(tag))
        .reduce((sum, item) => sum + item.value, 0);

      if (nonOverlappingValue > 0) {
        chartData.push({
          name: tag,
          value: nonOverlappingValue,
          itemStyle: { color: assignColor(tag, index) },
        });
      }
    });

    console.log('Transformed Chart Data for Pie:', chartData);
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