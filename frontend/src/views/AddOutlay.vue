<template>
  <div id="edit">
    <SideBar :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    <Header @toggle-menu="toggleMenu" />
    <div class="content">
      <AddMovementsData title="Add outlay" @confirm-transaction="onConfirmOutlay" />
      <OutlayTable />
    </div>
  </div>
</template>

<script>
import SideBar from '../components/SideBar.vue';
import Header from '../components/Header.vue';
import AddMovementsData from '../components/AddMovementsData.vue';
import OutlayTable from '../components/OutlayTable.vue';
import axios from 'axios';

export default {
  components: {
    SideBar,
    Header,
    AddMovementsData,
    OutlayTable,
  },
  data() {
    return {
      menuOpen: false,
      outlays: [],
    };
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
    async onConfirmOutlay(incomeData) {
      incomeData.tags = incomeData.tags || null;
      
      try {
        incomeData.type = "expense"
        const response = await axios.post(
          'http://localhost/api/addTransaction', // Use the correct URL with port if necessary
          incomeData, // Send incomeData directly
          {
            headers: { "Content-Type": "application/json" },
            withCredentials: true, // Include credentials if required
          }
        );
        console.log("Transaction added successfully:", response.data);
	this.loadOutlayTable();
      } catch (error) {
        console.error("Error adding transaction:", error.response ? error.response.data : error.message);
      }
    },
    async loadOutlayTable() {
      try {
        const response = await axios.get('http://localhost/api/getOutlays');
        this.outlays = response.data;  // Actualizar el estado de incomes con la respuesta del servidor
      } catch (error) {
        console.error("Error fetching outlay data:", error.message);
      }
    },
  },
  
  mounted() {
    // Al montar el componente, cargar los ingresos
    this.loadOutlayTable();
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