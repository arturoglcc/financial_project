<template>
  <div class="outlay-table">
    <h3>Outlays</h3>
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
        <tr v-for="outlay in outlays" :key="outlay.id">
          <td>
            <span v-if="!outlay.isEditing">
            <!-- Display tags as a comma-separated list -->
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
            <button @click="editOutlay(outlay)" v-if="!outlay.isEditing">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path stroke-dasharray="56" stroke-dashoffset="56" d="M3 21l2 -6l11 -11c1 -1 3 -1 4 0c1 1 1 3 0 4l-11 11l-6 2"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="56;0"/></path><path stroke-dasharray="8" stroke-dashoffset="8" d="M15 5l4 4"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s" values="8;0"/></path><path stroke-dasharray="6" stroke-dashoffset="6" stroke-width="1" d="M6 15l3 3"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s" values="6;0"/></path></g></svg>
            </button>

            <button @click="cancelEdit(outlay)" v-if="outlay.isEditing">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-dasharray="12" stroke-dashoffset="12" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 12l7 7M12 12l-7 -7M12 12l-7 7M12 12l7 -7"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.3s" values="12;0"/></path></svg>
            </button>

            <button @click="confirmOutlay(outlay)" v-if="outlay.isEditing">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-dasharray="24" stroke-dashoffset="24" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 11l6 6l10 -10"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.4s" values="24;0"/></path></svg>
            </button>

            <button @click="deleteOutlay(outlay.id)" v-if="outlay.isEditing">
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
      outlays: [],
    };
  },
  methods: {
    async fetchOutlays() {
      try {
        // Fetch incomes from the backend
        const response = await axios.get("http://localhost/api/allExpenses", {
          withCredentials: true, // Include credentials if authentication is required
        });
        this.outlays = response.data.map(expense => ({
          ...expense,
          tagsString: expense.tags ? expense.tags.join(", ") : "", // String format for editing
          isEditing: false,
        }));
      } catch (error) {
        console.error("Error fetching outlay:", error.response ? error.response.data : error.message);
      }
    },
    updateTags(outlay) {
      // Update tags array based on the input string
      outlay.tags = outlay.tagsString.split(",").map(tag => tag.trim());
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

  // Prepare the updated transaction data
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

    // On success, update the outlay in the local state
    Object.assign(outlay, updatedOutlay); // Update the outlay with new data
    outlay.isEditing = false;
    console.log(`Outlay updated successfully: ${response.data}`);
  } catch (error) {
    console.error("Error updating outlay:", error.response ? error.response.data : error.message);
  }
}
,
    deleteOutlay(id) {
  axios.delete(`http://localhost/api/deleteIncome/${id}`, {
    withCredentials: true, // Include credentials if needed
  })
  .then(response => {
    // Successfully deleted from the backend, remove from local data
    this.outlays = this.outlays.filter(outlay => outlay.id !== id);
    console.log(`Deleted outlay with id: ${id}`);
  })
  .catch(error => {
    console.error("Error deleting outlay:", error.response ? error.response.data : error.message);
  });
}

  },
  mounted() {
    this.fetchOutlays(); // Fetch data when the component is mounted
  },
};
</script>

<style scoped>
.outlay-table {
  margin: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}

.outlay-table h3 {
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
