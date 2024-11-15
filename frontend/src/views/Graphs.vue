<template>
  <div id="home">
    <SideBar :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    <Header @toggle-menu="toggleMenu" />
    <div class="content">
      <DayChart />
      <ChartsContainer />
    </div>
  </div>
</template>

<script>
import SideBar from '../components/SideBar.vue';
import Header from '../components/Header.vue';
import DayChart from '../components/DayChart.vue';
import ChartsContainer from '../components/ChartsContainer.vue';

export default {
  components: {
    SideBar,
    Header,
    DayChart,
    ChartsContainer,
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
</style>