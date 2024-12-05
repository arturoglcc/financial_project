<template>
  <div id="home">
    <SideBar :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    <Header @toggle-menu="toggleMenu" />
    <div class="content">
      <StatsContainer />
      <div class="graph-calendar">
        <div class="chart-item">
          <YearChart class="chart" />
        </div>
        <ScheduleMail />
      </div>
      <AddMovements />
    </div>
  </div>
</template>

<script>
import SideBar from '../components/SideBar.vue';
import Header from '../components/Header.vue';
import StatsContainer from '../components/StatsContainer.vue';
import AddMovements from '../components/AddMovements.vue';
import ScheduleMail from '../components/ScheduleMail.vue';
import YearChart from '../components/YearChart.vue';

export default {
  components: {
    SideBar,
    Header,
    StatsContainer,
    AddMovements,
    YearChart,
    ScheduleMail,
  },
  data() {
    return {
      menuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
  },
};
</script>


<style scoped>
#home {
  display: flex;
  height: 100vh;
}

.content {
  margin-left: 60px;
  transition: margin-left 0.3s ease;
  padding: 20px;
  flex-grow: 1;
  margin-top: 50px;
}

#home .sidebarExpanded + .content {
  margin-left: 240px;
}

.graph-calendar {
  margin-left: 27px;
  display: grid;
  grid-template-columns: 788px auto;
  gap: 20px;
  padding: 20px;
}

.chart-item {
  background-color: #fff;
  border-radius: 10px;
  border: 1px solid #ccc;
  padding: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
}

.chart {
  height: 400px;
}
</style>