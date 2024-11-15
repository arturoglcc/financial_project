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

    const generateRandomData = (points) => {
      return Array.from({ length: points }, () => Math.floor(Math.random() * 10000));
    };

    const initChart = () => {
      const chartInstance = echarts.init(chartRef.value);

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
          data: ['0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00'],
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
            data: generateRandomData(25),
          },
          {
            name: 'Outlays',
            type: 'line',
            data: generateRandomData(25),
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

    onMounted(() => {
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