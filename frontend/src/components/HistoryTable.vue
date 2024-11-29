<template>
  <div class="history-table">
    <div class="header">
      <h3>History</h3>
      <div class="filters">
        <input
          type="text"
          v-model="searchQuery"
          placeholder="Tags"
        />
        <input
          type="date"
          v-model="filterDate"
        />
      </div>
    </div>
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
        <tr
          v-for="movement in filteredMovements"
          :key="movement.id"
        >
          <td>
            <span v-if="!movement.isEditing">{{ movement.tag }}</span>
            <input v-else v-model="movement.tag" />
          </td>
          <td>{{ movement.type }}</td>
          <td>
            <span v-if="!movement.isEditing">{{ formatCurrency(movement.amount) }}</span>
            <input v-else type="number" v-model="movement.amount" />
          </td>
          <td>
            <span v-if="!movement.isEditing">{{ formatDate(movement.date) }}</span>
            <input v-else type="datetime-local" v-model="movement.date" />
          </td>
          <td>
            <span v-if="!movement.isEditing">{{ movement.description || "-------------------------" }}</span>
            <input v-else v-model="movement.description" />
          </td>
          <td>
            <button @click="editMovement(movement)" v-if="!movement.isEditing">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path stroke-dasharray="56" stroke-dashoffset="56" d="M3 21l2 -6l11 -11c1 -1 3 -1 4 0c1 1 1 3 0 4l-11 11l-6 2"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="56;0"/></path><path stroke-dasharray="8" stroke-dashoffset="8" d="M15 5l4 4"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s" values="8;0"/></path><path stroke-dasharray="6" stroke-dashoffset="6" stroke-width="1" d="M6 15l3 3"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s" values="6;0"/></path></g></svg>
            </button>

            <button @click="cancelEdit(movement)" v-if="movement.isEditing">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-dasharray="12" stroke-dashoffset="12" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 12l7 7M12 12l-7 -7M12 12l-7 7M12 12l7 -7"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.3s" values="12;0"/></path></svg>
            </button>

            <button @click="confirmMovement(movement)" v-if="movement.isEditing">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-dasharray="24" stroke-dashoffset="24" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 11l6 6l10 -10"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.4s" values="24;0"/></path></svg>
            </button>

            <button @click="deleteMovement(movement.id)">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="currentColor" d="M9 3v1H4v2h1v13a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6h1V4h-5V3zM7 6h10v13H7zm2 2v9h2V8zm4 0v9h2V8z"/></svg>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: "",
      filterDate: "",
      movements: [
        {
          id: 1,
          tag: "scholarship",
          type: "Income",
          amount: 1000.0,
          date: "2021-05-19T10:10:00",
          description: "",
          isEditing: false
        },
        {
          id: 2,
          tag: "Food",
          type: "Outlay",
          amount: 350.0,
          date: "2021-05-18T15:12:00",
          description: "",
          isEditing: false
        },
        {
          id: 3,
          tag: "Meeting",
          type: "Outlay",
          amount: 435.5,
          date: "2021-05-17T14:15:00",
          description: "",
          isEditing: false
        },
	{
          id: 4,
          tag: "Scholarship",
          type: "Income",
          amount: 1000.5,
          date: "2021-06-17T14:17:00",
          description: "",
          isEditing: false
        },
	{
          id: 5,
          tag: "Home",
          type: "Outlay",
          amount: 250.5,
          date: "2021-07-17T14:13:00",
          description: "",
          isEditing: false
        },
	{
          id: 6,
          tag: "Food",
          type: "Outlay",
          amount: 100.5,
          date: "2021-08-17T14:12:00",
          description: "",
          isEditing: false
        },
	{
          id: 7,
          tag: "Scholarship",
          type: "Income",
          amount: 1000.5,
          date: "2021-09-17T14:10:00",
          description: "",
          isEditing: false
        },
	{
          id: 8,
          tag: "Home",
          type: "Outlay",
          amount: 45.5,
          date: "2021-09-17T14:11:00",
          description: "",
          isEditing: false
        },
	{
          id: 9,
          tag: "Food",
          type: "Outlay",
          amount: 45.5,
          date: "2021-10-17T14:14:00",
          description: "",
          isEditing: false
        },
	{
          id: 10,
          tag: "Cinema",
          type: "Outlay",
          amount: 150.5,
          date: "2021-10-17T14:12:00",
          description: "",
          isEditing: false
        },
	{
          id: 11,
          tag: "Scholarship",
          type: "Income",
          amount: 1000.5,
          date: "2021-11-17T14:18:00",
          description: "",
          isEditing: false
        }
      ]
    };
  },
  computed: {
    filteredMovements() {
      let result = this.movements;

      if (this.searchQuery) {
        result = result.filter(movement =>
          movement.tag.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }

      if (this.filterDate) {
        result = result.filter(
          movement =>
            new Date(movement.date).toLocaleDateString() ===
            new Date(this.filterDate).toLocaleDateString()
        );
      }

      return result;
    }
  },
  methods: {
    formatCurrency(amount) {
      return `$ ${amount.toFixed(2)}`;
    },
    formatDate(date) {
      const options = { year: "numeric", month: "long", day: "numeric", hour: "2-digit", minute: "2-digit" };
      return new Date(date).toLocaleString("en-US", options);
    },
    editMovement(movement) {
      movement.originalData = { ...movement };
      movement.isEditing = true;
    },
    cancelEdit(movement) {
      Object.assign(movement, movement.originalData);
      movement.isEditing = false;
      movement.originalData = null;
    },
    confirmMovement(movement) {
      if (!movement.tag || movement.amount === null || !movement.date || !movement.description) {
        alert("All fields must be filled out before confirming.");
        return;
      }
      movement.isEditing = false;
    },
    deleteMovement(id) {
      this.movements = this.movements.filter(movement => movement.id !== id);
    }
  }
};
</script>

<style scoped>
.income-table {
  margin: 20px;
  font-family: Arial, sans-serif;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

.filters {
  display: flex;
  gap: 10px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

th, td {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

th {
  background: #f4f4f4;
}

button {
  cursor: pointer;
  border: none;
  background: transparent;
}

button:hover {
  color: gray;
}
</style>
