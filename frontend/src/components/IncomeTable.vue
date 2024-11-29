<template>
  <div class="income-table">
    <h3>Incomes</h3>
    <table>
      <thead>
        <tr>
          <th>Tags</th>
          <th>Type</th>
          <th>Amount</th>
          <th>Date</th>
          <th>Description</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="income in incomes" :key="income.id">
          <td>
            <span v-if="!income.isEditing">
            <!-- Display tags as a comma-separated list -->
            {{ income.tags && income.tags.length ? income.tags.join(", ") : "No tags" }}
            </span>
          <div v-else>
            <input
              v-model="income.tagsString"
              placeholder="Comma-separated tags"
              @input="updateTags(income)"
            />
          </div>
          </td>
          <td>{{ income.type }}</td>
          <td><span v-if="!income.isEditing">{{ formatCurrency(income.amount) }}</span>
            <input v-else type="number" v-model="income.amount" /></td>
          <td><span v-if="!income.isEditing">{{ formatDate(income.date_time) }}</span>
            <input v-else type="datetime-local" v-model="income.date_time" /></td>
          <td><span v-if="!income.isEditing">{{ income.description || "-------------------------" }}</span>
            <input v-else v-model="income.description" /></td>
          <td>
            <button @click="editIncome(income)" v-if="!income.isEditing">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path stroke-dasharray="56" stroke-dashoffset="56" d="M3 21l2 -6l11 -11c1 -1 3 -1 4 0c1 1 1 3 0 4l-11 11l-6 2"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="56;0"/></path><path stroke-dasharray="8" stroke-dashoffset="8" d="M15 5l4 4"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s" values="8;0"/></path><path stroke-dasharray="6" stroke-dashoffset="6" stroke-width="1" d="M6 15l3 3"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s" values="6;0"/></path></g></svg>
            </button>

            <button @click="cancelEdit(income)" v-if="income.isEditing">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-dasharray="12" stroke-dashoffset="12" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 12l7 7M12 12l-7 -7M12 12l-7 7M12 12l7 -7"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.3s" values="12;0"/></path></svg>
            </button>

            <button @click="confirmIncome(income)" v-if="income.isEditing">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-dasharray="24" stroke-dashoffset="24" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 11l6 6l10 -10"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.4s" values="24;0"/></path></svg>
            </button>

            <button @click="deleteIncome(income.id)" v-if="income.isEditing">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="currentColor" d="M9 3v1H4v2h1v13a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6h1V4h-5V3zM7 6h10v13H7zm2 2v9h2V8zm4 0v9h2V8z"/></svg>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      incomes: [],
    };
  },
  methods: {
    async fetchIncomes() {
      try {
        // Fetch incomes from the backend
        const response = await axios.get("http://localhost/api/allIncomes", {
          withCredentials: true, // Include credentials if authentication is required
        });
        this.incomes = response.data.map(income => ({
          ...income,
          tagsString: income.tags ? income.tags.join(", ") : "", // String format for editing
          isEditing: false,
        }));
      } catch (error) {
        console.error("Error fetching incomes:", error.response ? error.response.data : error.message);
      }
    },
    updateTags(income) {
      // Update tags array based on the input string
      income.tags = income.tagsString.split(",").map(tag => tag.trim());
    },
    formatCurrency(amount) {
      return `$ ${amount.toFixed(2)}`;
    },
    formatDate(date) {
      const options = { year: "numeric", month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" };
      return new Date(date).toLocaleString("en-US", options);
    },
    editIncome(income) {
      income.originalData = { ...income };
      income.isEditing = true;
    },
    cancelEdit(income) {
      Object.assign(income, income.originalData);
      income.isEditing = false;
      income.originalData = null;
    },
    async confirmIncome(income) {
  if (!income.tags || income.amount === null || !income.date_time || !income.description) {
    alert("All fields must be filled out before confirming.");
    return;
  }

  // Prepare the updated transaction data
  const updatedIncome = {
    id: income.id,
    tags: income.tags,
    amount: income.amount,
    date_time: income.date_time,
    description: income.description,
  };

  try {
    const response = await axios.put(
      `http://localhost/api/editTransaction/${income.id}`,
      updatedIncome,
      { withCredentials: true }
    );

    // On success, update the income in the local state
    Object.assign(income, updatedIncome); // Update the income with new data
    income.isEditing = false;
    console.log(`Income updated successfully: ${response.data}`);
  } catch (error) {
    console.error("Error updating income:", error.response ? error.response.data : error.message);
  }
}
,
    deleteIncome(id) {
  // Make an API call to the backend to delete the income
  axios.delete(`http://localhost/api/deleteIncome/${id}`, {
    withCredentials: true, // Include credentials if needed for authentication
  })
  .then((response) => {
    // If deletion was successful, filter out the deleted income from the local state
    this.incomes = this.incomes.filter(income => income.id !== id);
    console.log(`Deleted income with id: ${id}`);
  })
  .catch((error) => {
    console.error("Error deleting income:", error.response ? error.response.data : error.message);
  });
}

  },
  mounted() {
    this.fetchIncomes(); // Fetch data when the component is mounted
  },
};
</script>

<style scoped>
.income-table {
  margin: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}

.income-table h3 {
  margin-left: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f9f9f9;
}

td button {
  border: none;
  background: none;
  cursor: pointer;
  font-size: 1.2em;
  margin: 0 5px;
}

td button:hover svg {
  fill: #007bff;
}
</style>
