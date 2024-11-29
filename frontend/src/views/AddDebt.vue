<template>
  <div id="edit">
    <SideBar :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    <Header @toggle-menu="toggleMenu" />
    <div class="content">
      <AddDebtData />
      <DebtTable />
    </div>
  </div>
</template>

<script>
import SideBar from '../components/SideBar.vue';
import Header from '../components/Header.vue';
import AddDebtData from '../components/AddDebtData.vue';
import DebtTable from '../components/DebtTable.vue';
export default {
  components: {
    SideBar,
    Header,
    AddDebtData,
    DebtTable,
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
#edit {
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

#edit .sidebarExpanded + .content {
  margin-left: 240px;
}
</style>