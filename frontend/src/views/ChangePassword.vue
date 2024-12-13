<template>
  <!-- Page where the components to change the password are displayed -->
  <div id="edit">
    <SideBar :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    <Header @toggle-menu="toggleMenu" />
    <div class="content">
      <EditPassword />
    </div>
  </div>
</template>

<script>
import SideBar from '../components/SideBar.vue';
import Header from '../components/Header.vue';
import EditPassword from '../components/EditPassword.vue';
export default {
  components: {
    SideBar,
    Header,
    EditPassword,
  },
  data() {
    return {
      menuOpen: false,
    };
  },
  methods: {
    // Toggle the sidebar menu open/close state
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

#edit .sidebarExpanded+.content {
  margin-left: 240px;
}
</style>