<template>
  <div class="debt-table">
    <h3>Debts</h3>
    <table>
      <thead>
        <tr>
          <th>Creditor</th>
          <th>Type</th>
          <th>Interest-free months</th>
          <th>Amount</th>
          <th>Date</th>
          <th>Description</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="debt in debts" :key="debt.id">
          <td>
            <span v-if="!debt.isEditing">{{ debt.creditor }}</span>
            <input v-else v-model="debt.creditor"/>
          </td>
          <td>{{ debt.type }}</td>
          <td>
            <span v-if="!debt.isEditing">{{ debt.months }}</span>
            <input v-else type="number" min="0" v-model="debt.months"/>
          </td>
          <td>
            <span v-if="!debt.isEditing">{{ formatCurrency(debt.amount) }}</span>
            <input v-else type="number" v-model="debt.amount"/>
          </td>
          <td>
            <span v-if="!debt.isEditing">{{ formatDate(debt.date) }}</span>
            <input v-else type="datetime-local" v-model="debt.date"/>
          </td>
          <td>
            <span v-if="!debt.isEditing">{{ debt.description || "-------------------------" }}</span>
            <input v-else v-model="debt.description"/>
          </td>
          <td>
            <button @click="editDebt(debt)" v-if="!debt.isEditing">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path stroke-dasharray="56" stroke-dashoffset="56" d="M3 21l2 -6l11 -11c1 -1 3 -1 4 0c1 1 1 3 0 4l-11 11l-6 2"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="56;0"/></path><path stroke-dasharray="8" stroke-dashoffset="8" d="M15 5l4 4"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s" values="8;0"/></path><path stroke-dasharray="6" stroke-dashoffset="6" stroke-width="1" d="M6 15l3 3"><animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s" values="6;0"/></path></g></svg>
            </button>

            <button @click="cancelEdit(debt)" v-if="debt.isEditing">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-dasharray="12" stroke-dashoffset="12" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 12l7 7M12 12l-7 -7M12 12l-7 7M12 12l7 -7"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.3s" values="12;0"/></path></svg>
            </button>

            <button @click="confirmDebt(debt)" v-if="debt.isEditing">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-dasharray="24" stroke-dashoffset="24" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 11l6 6l10 -10"><animate fill="freeze" attributeName="stroke-dashoffset" dur="0.4s" values="24;0"/></path></svg>
            </button>

            <button @click="deleteDebt(debt.id)" v-if="debt.isEditing">
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
      debts: []
    };
  },
  methods: {
    formatCurrency(amount) {
      return `$ ${amount.toFixed(2)}`;
    },
    formatDate(date) {
      const options = { year: "numeric", month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" };
      return new Date(date).toLocaleString("en-US", options);
    },
    addDebt(newDebt) {
      this.debts.push(newDebt);
    },
    editDebt(debt) {
      debt.originalData = { ...debt };
      debt.isEditing = true;
    },
    cancelEdit(debt) {
      Object.assign(debt, debt.originalData);
      debt.isEditing = false;
      debt.originalData = null;
    },
    confirmDebt(debt) {
      if (!debt.creditor || debt.months === null || debt.amount === null || !debt.date || !debt.description) {
        alert("All fields must be filled out before confirming.");
        return;
      }
      debt.isEditing = false;
      console.log(`Confirmed debt with id: ${debt.id}`);
    },
    deleteDebt(id) {
      this.debts = this.debts.filter(debt => debt.id !== id);
      console.log(`Deleted debt with id: ${id}`);
    }
  }
};
</script>

<style scoped>
.debt-table {
  margin: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}

.debt-table h3 {
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