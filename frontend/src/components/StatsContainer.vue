<template>
  <div class="stats-container">
    <div class="stat-card dark">
      <div class="stat-title">
        Last outlay
      </div>
      <div class="stat-value">
        $ {{ lastOutlay}}
      </div>
      <div class="stat-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 20 20">
          <path fill="currentColor" d="M10.6 9c-.4-.1-.8-.3-1.1-.6c-.3-.1-.4-.4-.4-.6s.1-.5.3-.6c.3-.2.6-.4.9-.3c.6 0 1.1.3 1.4.7l.9-1.2c-.3-.3-.6-.5-.9-.7s-.7-.3-1.1-.3V4H9.4v1.4c-.5.1-1 .4-1.4.8c-.4.5-.7 1.1-.6 1.7c0 .6.2 1.2.6 1.6c.5.5 1.2.8 1.8 1.1c.3.1.7.3 1 .5c.2.2.3.5.3.8q0 .45-.3.9c-.3.3-.7.4-1 .4c-.4 0-.9-.1-1.2-.4c-.3-.2-.6-.5-.8-.8l-1 1.1c.3.4.6.7 1 1c.5.3 1.1.6 1.7.6V16h1.1v-1.5c.6-.1 1.1-.4 1.5-.8c.5-.5.8-1.3.8-2c0-.6-.2-1.3-.7-1.7c-.5-.5-1-.8-1.6-1M10 2c-4.4 0-8 3.6-8 8s3.6 8 8 8s8-3.6 8-8s-3.6-8-8-8m0 14.9c-3.8 0-6.9-3.1-6.9-6.9S6.2 3.1 10 3.1s6.9 3.1 6.9 6.9s-3.1 6.9-6.9 6.9" />
        </svg>
      </div>
    </div>
    <div class="stat-card light">
      <div class="stat-title">
        Last income
      </div>
      <div class="stat-value">
        $ {{ lastIncome}}
      </div>
      <div class="stat-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 20 20">
          <path fill="currentColor" d="M10.6 9c-.4-.1-.8-.3-1.1-.6c-.3-.1-.4-.4-.4-.6s.1-.5.3-.6c.3-.2.6-.4.9-.3c.6 0 1.1.3 1.4.7l.9-1.2c-.3-.3-.6-.5-.9-.7s-.7-.3-1.1-.3V4H9.4v1.4c-.5.1-1 .4-1.4.8c-.4.5-.7 1.1-.6 1.7c0 .6.2 1.2.6 1.6c.5.5 1.2.8 1.8 1.1c.3.1.7.3 1 .5c.2.2.3.5.3.8q0 .45-.3.9c-.3.3-.7.4-1 .4c-.4 0-.9-.1-1.2-.4c-.3-.2-.6-.5-.8-.8l-1 1.1c.3.4.6.7 1 1c.5.3 1.1.6 1.7.6V16h1.1v-1.5c.6-.1 1.1-.4 1.5-.8c.5-.5.8-1.3.8-2c0-.6-.2-1.3-.7-1.7c-.5-.5-1-.8-1.6-1M10 2c-4.4 0-8 3.6-8 8s3.6 8 8 8s8-3.6 8-8s-3.6-8-8-8m0 14.9c-3.8 0-6.9-3.1-6.9-6.9S6.2 3.1 10 3.1s6.9 3.1 6.9 6.9s-3.1 6.9-6.9 6.9" />
        </svg>
      </div>
    </div>
    <div class="stat-card dark">
      <div class="stat-title">
        Debt
      </div>
      <div class="stat-value">
        $ 0
      </div>
      <div class="stat-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 20 20">
          <path fill="currentColor" d="M10.6 9c-.4-.1-.8-.3-1.1-.6c-.3-.1-.4-.4-.4-.6s.1-.5.3-.6c.3-.2.6-.4.9-.3c.6 0 1.1.3 1.4.7l.9-1.2c-.3-.3-.6-.5-.9-.7s-.7-.3-1.1-.3V4H9.4v1.4c-.5.1-1 .4-1.4.8c-.4.5-.7 1.1-.6 1.7c0 .6.2 1.2.6 1.6c.5.5 1.2.8 1.8 1.1c.3.1.7.3 1 .5c.2.2.3.5.3.8q0 .45-.3.9c-.3.3-.7.4-1 .4c-.4 0-.9-.1-1.2-.4c-.3-.2-.6-.5-.8-.8l-1 1.1c.3.4.6.7 1 1c.5.3 1.1.6 1.7.6V16h1.1v-1.5c.6-.1 1.1-.4 1.5-.8c.5-.5.8-1.3.8-2c0-.6-.2-1.3-.7-1.7c-.5-.5-1-.8-1.6-1M10 2c-4.4 0-8 3.6-8 8s3.6 8 8 8s8-3.6 8-8s-3.6-8-8-8m0 14.9c-3.8 0-6.9-3.1-6.9-6.9S6.2 3.1 10 3.1s6.9 3.1 6.9 6.9s-3.1 6.9-6.9 6.9" />
        </svg>
      </div>
    </div>
    <div class="stat-card light">
      <div class="stat-title">
        Balance
      </div>
      <div class="stat-value">
        $ 0
      </div>
      <div class="stat-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 20 20">
          <path fill="currentColor" d="M10.6 9c-.4-.1-.8-.3-1.1-.6c-.3-.1-.4-.4-.4-.6s.1-.5.3-.6c.3-.2.6-.4.9-.3c.6 0 1.1.3 1.4.7l.9-1.2c-.3-.3-.6-.5-.9-.7s-.7-.3-1.1-.3V4H9.4v1.4c-.5.1-1 .4-1.4.8c-.4.5-.7 1.1-.6 1.7c0 .6.2 1.2.6 1.6c.5.5 1.2.8 1.8 1.1c.3.1.7.3 1 .5c.2.2.3.5.3.8q0 .45-.3.9c-.3.3-.7.4-1 .4c-.4 0-.9-.1-1.2-.4c-.3-.2-.6-.5-.8-.8l-1 1.1c.3.4.6.7 1 1c.5.3 1.1.6 1.7.6V16h1.1v-1.5c.6-.1 1.1-.4 1.5-.8c.5-.5.8-1.3.8-2c0-.6-.2-1.3-.7-1.7c-.5-.5-1-.8-1.6-1M10 2c-4.4 0-8 3.6-8 8s3.6 8 8 8s8-3.6 8-8s-3.6-8-8-8m0 14.9c-3.8 0-6.9-3.1-6.9-6.9S6.2 3.1 10 3.1s6.9 3.1 6.9 6.9s-3.1 6.9-6.9 6.9" />
        </svg>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      lastIncome: null, // Store the value of the last income
      lastOutlay: null, // Store the value of the last outlay
    };
  },
  methods: {
    async fetchStats() {
      try {
        // Fetch last income
        const incomeResponse = await axios.get("http://localhost/api/lastIncome", {
          withCredentials: true, // Include credentials if authentication is required
        });
        this.lastIncome = incomeResponse.data.amount;
      } catch (error) {
        console.error("Error fetching last income:", error.response ? error.response.data : error.message);
        this.lastIncome = 0; // Set fallback value for income only
      }

      try {
        // Fetch last outlay (expense)
        const outlayResponse = await axios.get("http://localhost/api/lastExpense", {
          withCredentials: true, // Include credentials if authentication is required
        });
        this.lastOutlay = outlayResponse.data.amount;
      } catch (error) {
        console.error("Error fetching last outlay:", error.response ? error.response.data : error.message);
        this.lastOutlay = 0; // Set fallback value for outlay only
      }
    },
  },
  mounted() {
    this.fetchStats(); // Fetch data when the component is mounted
  },
};
</script>

<style scoped>
.stats-container {
  display: flex;
  justify-content: center;
  gap: 10px;
}

.stat-card {
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 15px;
  width: 250px;
  height: 100px;
  text-align: left;
  position: relative;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
}

.stat-card.dark {
  background-color: #333;
  color: white;
}

.stat-card.light {
  background-color: white;
  color: #333;
}

.stat-title {
  font-weight: bold;
  font-size: 25px;
}

.stat-value {
  font-size: 25px;
  margin-top: 5px;
}

.stat-icon {
  position: absolute;
  top: 10px;
  right: 20px;
  font-size: 2.5em;
}
</style>