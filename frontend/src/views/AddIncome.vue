<template>
  <!-- Page showing the components to add income -->
  <div id="edit">
    <SideBar :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    <Header @toggle-menu="toggleMenu" />
    <div class="content">
      <AddMovementsData title="Add income" @confirm-transaction="onConfirmIncome" />
      <IncomeTable ref="incomeTable" />
    </div>
  </div>
</template>

<script>
import SideBar from '../components/SideBar.vue';
import Header from '../components/Header.vue';
import AddMovementsData from '../components/AddMovementsData.vue';
import IncomeTable from '../components/IncomeTable.vue';
import axios from 'axios';

export default {
  components: {
    SideBar,
    Header,
    AddMovementsData,
    IncomeTable,
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
    // Handle the confirmation of a new income transaction
    async onConfirmIncome(incomeData) {
      incomeData.tags = incomeData.tags || null;
      try {
        incomeData.type = "income"
        const response = await axios.post(
          'http://localhost/api/addTransaction', // Use the correct URL with port if necessary
          incomeData, // Send incomeData directly
          {
            headers: { "Content-Type": "application/json" },
            withCredentials: true, // Include credentials if required
          }
        );
        console.log("Transaction added successfully:", response.data);
        this.$refs.incomeTable.fetchIncomes();
      } catch (error) {
        console.error("Error adding transaction:", error.response ? error.response.data : error.message);
      }
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