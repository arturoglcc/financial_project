<template>
  <!-- Page where the components are displayed so that user information can be changed. -->
  <div id="edit">
    <SideBar :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    <Header @toggle-menu="toggleMenu" />
    <div class="content">
      <EditProfile />
    </div>
  </div>
</template>

<script>
import SideBar from '../components/SideBar.vue';
import Header from '../components/Header.vue';
import EditProfile from '../components/EditProfile.vue';
export default {
  components: {
    SideBar,
    Header,
    EditProfile,
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