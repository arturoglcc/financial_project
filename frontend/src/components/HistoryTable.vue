<template>
  <div>
    <button @click="toggleHistory" class="switch-button">
      <i class="fas" :class="isIncome ? 'fa-arrow-right' : 'fa-arrow-left'"></i>
      Switch to {{ isIncome ? 'Outlays' : 'Incomes' }}
    </button>

        <!-- Search Bar -->
        <div class="search-bar">
      <input 
        type="text" 
        v-model="searchQuery" 
        placeholder="Search by tags or description..." 
        class="search-input"
      />
    </div>

    <!-- Outlay Table -->
    <div v-if="!isIncome" class="transaction-table outlay-table">
      <h3><i class="fas fa-money-bill-wave"></i> Outlays</h3>
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
          <tr v-for="outlay in filteredOutlays" :key="outlay.id">
            <td>
              <span v-if="!outlay.isEditing">
                {{ outlay.tags && outlay.tags.length ? outlay.tags.join(", ") : "No tags" }}
              </span>
              <div v-else>
                <input
                  v-model="outlay.tagsString"
                  placeholder="Comma-separated tags"
                  @input="updateTags(outlay)"
                />
              </div>
            </td>
            <td>{{ outlay.type }}</td>
            <td><span v-if="!outlay.isEditing">{{ formatCurrency(outlay.amount) }}</span>
              <input v-else type="number" v-model="outlay.amount" /></td>
            <td><span v-if="!outlay.isEditing">{{ formatDate(outlay.date_time) }}</span>
              <input v-else type="datetime-local" v-model="outlay.date_time" /></td>
            <td><span v-if="!outlay.isEditing">{{ outlay.description || "-------------------------" }}</span>
              <input v-else v-model="outlay.description" /></td>
            <td>
              <button @click="editOutlay(outlay)">
                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path stroke-dasharray="56" stroke-dashoffset="56" d="M3 21l2 -6l11 -11c1 -1 3 -1 4 0c1 1 1 3 0 4l-11 11l-6 2"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="56;0"/></path><path stroke-dasharray="8" stroke-dashoffset="8" d="M15 5l4 4"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s" values="8;0"/></path><path stroke-dasharray="6" stroke-dashoffset="6" stroke-width="1" d="M6 15l3 3"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s" values="6;0"/></path></g></svg>
            </button>

              <button @click="cancelEdit(outlay)" v-if="outlay.isEditing"><i class="fas fa-times"></i> 
                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-dasharray="12" stroke-dashoffset="12" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 12l7 7M12 12l-7 -7M12 12l-7 7M12 12l7 -7"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.3s" values="12;0"/></path></svg>
              </button>

              <button @click="confirmOutlay(outlay)" v-if="outlay.isEditing"><i class="fas fa-check"></i> 
                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-dasharray="24" stroke-dashoffset="24" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 11l6 6l10 -10"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.4s" values="24;0"/></path></svg>
              </button>

              <button @click="deleteOutlay(outlay.id)"><i class="fas fa-trash-alt"></i> 
                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="currentColor" d="M9 3v1H4v2h1v13a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6h1V4h-5V3zM7 6h10v13H7zm2 2v9h2V8zm4 0v9h2V8z"/></svg>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Income Table -->
    <div v-else class="transaction-table income-table">
      <h3><i class="fas fa-coins"></i> Incomes</h3>
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
          <tr v-for="income in filteredIncomes" :key="income.id">
            <td>
              <span v-if="!income.isEditing">
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
              <button @click="editOutlay(income)">
                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path stroke-dasharray="56" stroke-dashoffset="56" d="M3 21l2 -6l11 -11c1 -1 3 -1 4 0c1 1 1 3 0 4l-11 11l-6 2"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="56;0"/></path><path stroke-dasharray="8" stroke-dashoffset="8" d="M15 5l4 4"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s" values="8;0"/></path><path stroke-dasharray="6" stroke-dashoffset="6" stroke-width="1" d="M6 15l3 3"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s" values="6;0"/></path></g></svg>
            </button>

              <button @click="cancelEdit(income)" v-if="income.isEditing"><i class="fas fa-times"></i> 
                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-dasharray="12" stroke-dashoffset="12" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 12l7 7M12 12l-7 -7M12 12l-7 7M12 12l7 -7"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.3s" values="12;0"/></path></svg>
              </button>

              <button @click="confirmOutlay(income)" v-if="income.isEditing"><i class="fas fa-check"></i> 
                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-dasharray="24" stroke-dashoffset="24" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 11l6 6l10 -10"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.4s" values="24;0"/></path></svg>
              </button>

              <button @click="deleteOutlay(income.id)"><i class="fas fa-trash-alt"></i> 
                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="currentColor" d="M9 3v1H4v2h1v13a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6h1V4h-5V3zM7 6h10v13H7zm2 2v9h2V8zm4 0v9h2V8z"/></svg>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      isIncome: false, // Tracks if we are viewing Incomes or Outlays
      incomes: [],
      outlays: [],
      searchQuery: "", // Stores the search input
    };
  },
  computed: {
  filteredOutlays() {
    if (!this.searchQuery) return this.outlays;

    // Process the search query: split by commas, trim spaces, and filter out empty strings
    const keywords = this.searchQuery
      .split(",")
      .map(keyword => keyword.trim())
      .filter(keyword => keyword);

    // Filter outlays by matching any of the keywords
    return this.outlays.filter(outlay => {
      const matchesTags = outlay.tags && outlay.tags.some(tag =>
        keywords.some(keyword => tag.toLowerCase().includes(keyword.toLowerCase()))
      );
      const matchesDescription = outlay.description && keywords.some(keyword =>
        outlay.description.toLowerCase().includes(keyword.toLowerCase())
      );
      return matchesTags || matchesDescription;
    });
  },
  filteredIncomes() {
    if (!this.searchQuery) return this.incomes;

    // Process the search query: split by commas, trim spaces, and filter out empty strings
    const keywords = this.searchQuery
      .split(",")
      .map(keyword => keyword.trim())
      .filter(keyword => keyword);

    // Filter incomes by matching any of the keywords
    return this.incomes.filter(income => {
      const matchesTags = income.tags && income.tags.some(tag =>
        keywords.some(keyword => tag.toLowerCase().includes(keyword.toLowerCase()))
      );
      const matchesDescription = income.description && keywords.some(keyword =>
        income.description.toLowerCase().includes(keyword.toLowerCase())
      );
      return matchesTags || matchesDescription;
    });
  },
},


  methods: {
    toggleHistory() {
      this.isIncome = !this.isIncome;
      this.fetchData(); // Refetch the data based on the selected history
    },
    async fetchData() {
      try {
        if (this.isIncome) {
          const response = await axios.get("http://localhost/api/allIncomes", {
            withCredentials: true, // Include credentials if authentication is required
          });
          this.incomes = response.data.map(income => ({
            ...income,
            tagsString: income.tags ? income.tags.join(", ") : "",
            isEditing: false,
          }));
        } else {
          const response = await axios.get("http://localhost/api/allExpenses", {
            withCredentials: true,
          });
          this.outlays = response.data.map(expense => ({
            ...expense,
            tagsString: expense.tags ? expense.tags.join(", ") : "",
            isEditing: false,
          }));
        }
      } catch (error) {
        console.error("Error fetching data:", error.response ? error.response.data : error.message);
      }
    },
    updateTags(transaction) {
      transaction.tags = transaction.tagsString.split(",").map(tag => tag.trim());
    },
    formatCurrency(amount) {
      return `$ ${amount.toFixed(2)}`;
    },
    formatDate(date) {
      const options = { year: "numeric", month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" };
      return new Date(date).toLocaleString("en-US", options);
    },
    editOutlay(outlay) {
      outlay.originalData = { ...outlay };
      outlay.isEditing = true;
    },
    cancelEdit(outlay) {
      Object.assign(outlay, outlay.originalData);
      outlay.isEditing = false;
      outlay.originalData = null;
    },
    async confirmOutlay(outlay) {
      if (!outlay.tags || outlay.amount === null || !outlay.date_time || !outlay.description) {
        alert("All fields must be filled out before confirming.");
        return;
      }
      const updatedOutlay = {
        id: outlay.id,
        tags: outlay.tags,
        amount: outlay.amount,
        date_time: outlay.date_time,
        description: outlay.description,
      };

      try {
        const response = await axios.put(
          `http://localhost/api/editTransaction/${outlay.id}`,
          updatedOutlay,
          { withCredentials: true }
        );

        Object.assign(outlay, updatedOutlay);
        outlay.isEditing = false;
        console.log(`Outlay updated successfully: ${response.data}`);
      } catch (error) {
        console.error("Error updating outlay:", error.response ? error.response.data : error.message);
      }
    },
    deleteOutlay(id) {
      axios.delete(`http://localhost/api/deleteIncome/${id}`, {
        withCredentials: true,
      })
        .then(response => {
          this.outlays = this.outlays.filter(outlay => outlay.id !== id);
          this.incomes = this.incomes.filter(income => income.id !== id);
          console.log(`Deleted outlay with id: ${id}`);
        })
        .catch(error => {
          console.error("Error deleting outlay:", error.response ? error.response.data : error.message);
        });
    },
    editIncome(income) {
      income.originalData = { ...income };
      income.isEditing = true;
    },
    cancelEditIncome(income) {
      Object.assign(income, income.originalData);
      income.isEditing = false;
      income.originalData = null;
    },
    async confirmIncome(income) {
      if (!income.tags || income.amount === null || !income.date_time || !income.description) {
        alert("All fields must be filled out before confirming.");
        return;
      }
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

        Object.assign(income, updatedIncome);
        income.isEditing = false;
        console.log(`Income updated successfully: ${response.data}`);
      } catch (error) {
        console.error("Error updating income:", error.response ? error.response.data : error.message);
      }
    },
    async deleteIncome(incomeId) {
  try {
    // Assuming you're calling an API to delete the income
    await axios.delete(`http://localhost/api/deleteIncome/${incomeId}`, {
      withCredentials: true,
    })
    .then(response => {
          this.incomes = this.incomes.filter(income => income.id !== id);
          console.log(`Deleted income with id: ${id}`);
        })
  } catch (error) {
    console.error("Error deleting income:", error);
  }
}

  },
  mounted() {
    this.fetchData(); // Initial data fetch
  },
};
</script>

<style scoped>

.search-bar {
  margin: 20px 0;
  text-align: center;
}

.search-input {
  width: 50%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1em;
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

/* Add custom widths to the columns */
th:nth-child(1), td:nth-child(1) { width: 20%; }  /* First column (Tags) */
th:nth-child(2), td:nth-child(2) { width: 15%; }  /* Second column (Type) */
th:nth-child(3), td:nth-child(3) { width: 15%; }  /* Third column (Amount) */
th:nth-child(4), td:nth-child(4) { width: 20%; }  /* Fourth column (Date) */
th:nth-child(5), td:nth-child(5) { width: 25%; }  /* Fifth column (Description) */
th:nth-child(6), td:nth-child(6) { width: 15%; }  /* Sixth column (Actions) */

.transaction-table {
  width: 100%; /* Makes the table take up all available width */
  max-width: 1200px; /* Optional: Restrict the maximum width */
  margin: 0 auto; /* Center the table */
  border-collapse: collapse; /* Optional: Makes the table borders more compact */
}

.transaction-table th,
.transaction-table td {
  padding: 15px; /* Increase padding for better spacing */
  text-align: left;
  border-bottom: 1px solid #ddd; /* Consistent border for all cells */
}

.transaction-table th {
  background-color: #f5f5f5; /* Optional: Adds a background color to headers */
}

.transaction-table td {
  background-color: #ffffff; /* Optional: Adds a background color to rows */
}

.switch-button {
  padding: 10px;
  margin: 10px;
  background-color: #000;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 10px;
}

.switch-button .fas {
  margin-right: 8px;
}

.income-table .fas {
  color: #2a9d8f;
}

.outlay-table .fas {
  color: #e76f51;
}
</style>
