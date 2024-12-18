<template>
  <div class="calendar-container">
    <h2>Schedule Mail</h2>
    <div class="calendar-header">
      <!-- Button to navigate to the previous month -->
      <button @click="prevMonth">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
          <path fill="none" stroke="currentColor" stroke-dasharray="12" stroke-dashoffset="12" stroke-linecap="round"
            stroke-linejoin="round" stroke-width="2" d="M8 12l7 -7M8 12l7 7">
            <animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="12;0" />
          </path>
        </svg>
      </button>
      <!-- Display the current month and year -->
      <span class="month-title">{{ currentMonthName }} {{ currentYear }}</span>
      <!-- Button to navigate to the next month -->
      <button @click="nextMonth">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
          <path fill="none" stroke="currentColor" stroke-dasharray="12" stroke-dashoffset="12" stroke-linecap="round"
            stroke-linejoin="round" stroke-width="2" d="M16 12l-7 -7M16 12l-7 7">
            <animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="12;0" />
          </path>
        </svg>
      </button>
    </div>
    <div class="calendar">
      <!-- Display the days of the week -->
      <div class="day-header" v-for="day in daysOfWeek" :key="day">{{ day }}</div>
      <!-- Display the days in the current month -->
      <div class="day" v-for="(day, index) in daysInMonth" :key="index"
        :class="{ 'selected': isSelected(day), 'highlighted': isHighlighted(day) }" @click="selectDate(day)">
        {{ day || '' }}
      </div>
    </div>
    <!-- Dropdown to select the frequency of the mail -->
    <select class="frequency-select" v-model="selectedFrequency" @change="calculateHighlightedDates">
      <option value="daily">Daily</option>
      <option value="weekly">Weekly</option>
      <option value="biweekly">Biweekly</option>
      <option value="monthly">Monthly</option>
      <option value="annual">Annual</option>
    </select>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentMonth: new Date().getMonth(),
      currentYear: new Date().getFullYear(),
      daysOfWeek: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
      selectedDate: null,
      selectedFrequency: 'monthly',
      highlightedDates: [],
    };
  },
  computed: {
    // Get the name of the current month
    currentMonthName() {
      return new Date(this.currentYear, this.currentMonth).toLocaleString('en-US', { month: 'long' });
    },
    // Get the days in the current month
    daysInMonth() {
      const firstDay = new Date(this.currentYear, this.currentMonth, 1).getDay();
      const daysInMonth = new Date(this.currentYear, this.currentMonth + 1, 0).getDate();
      return Array.from({ length: firstDay }, () => null).concat(Array.from({ length: daysInMonth }, (_, i) => i + 1));
    },
  },
  methods: {
    // Navigate to the previous month
    prevMonth() {
      if (this.currentMonth === 0) {
        this.currentMonth = 11;
        this.currentYear--;
      } else {
        this.currentMonth--;
      }
      this.calculateHighlightedDates();
    },
    // Navigate to the next month
    nextMonth() {
      if (this.currentMonth === 11) {
        this.currentMonth = 0;
        this.currentYear++;
      } else {
        this.currentMonth++;
      }
      this.calculateHighlightedDates();
    },
    // Select a date in the calendar
    selectDate(day) {
      if (!day) return;
      this.selectedDate = new Date(this.currentYear, this.currentMonth, day);
      this.calculateHighlightedDates();
    },
    // Check if a day is selected
    isSelected(day) {
      return this.selectedDate && this.selectedDate.getDate() === day && this.selectedDate.getMonth() === this.currentMonth && this.selectedDate.getFullYear() === this.currentYear;
    },
    // Check if a day is highlighted
    isHighlighted(day) {
      return this.highlightedDates.some(date => date.getDate() === day && date.getMonth() === this.currentMonth && date.getFullYear() === this.currentYear);
    },
    // Calculate the highlighted dates based on the selected frequency
    calculateHighlightedDates() {
      this.highlightedDates = [];
      if (!this.selectedDate) return;
      let currentDate = new Date(this.selectedDate);
      while (currentDate.getFullYear() <= this.currentYear + 1) {
        this.highlightedDates.push(new Date(currentDate));
        switch (this.selectedFrequency) {
          case 'daily':
            currentDate.setDate(currentDate.getDate() + 1);
            break;
          case 'weekly':
            currentDate.setDate(currentDate.getDate() + 7);
            break;
          case 'biweekly':
            currentDate.setDate(currentDate.getDate() + 14);
            break;
          case 'monthly':
            currentDate.setMonth(currentDate.getMonth() + 1);
            break;
          case 'annual':
            currentDate.setFullYear(currentDate.getFullYear() + 1);
            break;
        }
      }
    }
  },
  mounted() {
    this.selectDate(1); // Select the first day of the month by default
  }
};
</script>

<style scoped>
.calendar-container {
  max-width: 300px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #fff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h2 {
  margin-top: 1px;
  margin-bottom: 12px;
}

.calendar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.month-title {
  font-weight: bold;
  color: #333;
  font-size: 1.2rem;
}

.calendar-header button {
  background: none;
  border: none;
  cursor: pointer;
}

.calendar-header button svg {
  width: 24px;
  height: 24px;
}

.calendar {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 5px;
}

.day-header {
  text-align: center;
  font-weight: bold;
}

.day {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 40px;
  border-radius: 50%;
  cursor: pointer;
  transition: background-color 0.3s;
}

.day:hover {
  background-color: #e0e0e0;
}

.day.selected {
  background-color: #007bff;
  color: #fff;
}

.day.highlighted {
  background-color: #000000;
  color: #fff;
}

.frequency-select {
  margin-top: 10px;
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #9c9ea3;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  background-color: white;
  cursor: pointer;
}

.frequency-select:focus {
  outline: none;
  border-color: #525252;
}
</style>