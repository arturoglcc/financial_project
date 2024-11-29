<template>
  <div class="form-container">
    <h2>{{ title }}</h2>
    <form @submit.prevent="handleAdd">
      <div class="form-grid">
        <!-- Description Field -->
        <div class="form-control">
          <input type="text" required v-model="description">
          <label>
            <span style="transition-delay:0ms">D</span><span style="transition-delay:50ms">e</span><span style="transition-delay:100ms">s</span><span style="transition-delay:150ms">c</span><span style="transition-delay:200ms">r</span><span style="transition-delay:250ms">i</span><span style="transition-delay:300ms">p</span><span style="transition-delay:350ms">t</span><span style="transition-delay:400ms">i</span><span style="transition-delay:450ms">o</span><span style="transition-delay:500ms">n</span>
          </label>
        </div>

        <!-- Date Field -->
        <div class="form-control2">
          <label for="dateInput">Date</label>
          <input class="input-date-time" type="date" id="dateInput" v-model="dateInput" required />
        </div>

        <!-- Time Field -->
        <div class="form-control2">
          <label for="timeInput">Time</label>
          <input class="input-date-time" type="time" id="timeInput" v-model="timeInput" required />
        </div>

        <!-- Tags Field -->
        <div class="form-control">
          <input type="text" required v-model="tags">
          <label>
            <span style="transition-delay:0ms">T</span><span style="transition-delay:50ms">a</span><span style="transition-delay:100ms">g</span><span style="transition-delay:150ms">s</span>
          </label>
        </div>

        <!-- Amount Field, centered -->
        <div class="form-control amount-centered">
          <input type="float" required v-model="amount">
          <label>
            <span style="transition-delay:0ms">A</span><span style="transition-delay:50ms">m</span><span style="transition-delay:100ms">o</span><span style="transition-delay:150ms">u</span><span style="transition-delay:200ms">n</span><span style="transition-delay:250ms">t</span><span style="transition-delay:300ms"> </span><span style="transition-delay:350ms">$</span>
          </label>
        </div>

        <small>*Place the tags related to the entry separated by commas, for example: cinema, food <br> *Set the time in 24 hour format, for example, 22:15 <br> *Enter the amount with two decimal numbers, for example: 100.00</small>
        
        <!-- Confirm Button -->
        <button @click="handleConfirm"><span class="text">Confirm</span><span>Confirm</span></button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    title: {
      type: String,
      default: "Add Income",
    },
  },
  data() {
    return {
      description: "",
      dateInput: "",
      timeInput: "",
      tags: "",
      amount: ""
    };
  },
  methods: {
    handleConfirm() {
      if (!this.description || !this.dateInput || !this.timeInput || !this.amount) {
        alert("All fields must be filled out.");
        return;
      }
      console.log("A transaction has been sent");
      // Gather data into an object to emit to the parent
      const incomeData = {
        description: this.description,
        date_time: `${this.dateInput}T${this.timeInput}`, // Combine date and time into a single DateTime string
        amount: parseFloat(this.amount), // Convert amount to a number
        type: "",
      };

      // Only add tags to incomeData if tags input is not empty
      if (this.tags && this.tags.trim()) {
        incomeData.tags = this.tags.split(',').map(tag => tag.trim());
      }

      // Emit the data to the parent
      this.$emit("confirm-transaction", incomeData);
      setTimeout(() => 5000);
      this.description = "";
      this.dateInput = "";
      this.timeInput = "";
      this.tags = "";
      this.amount = "";
    },
  },
};
</script>

<style scoped>
.form-container {
  border: 2px solid #ddd;
  border-radius: 10px;
  padding: 20px;
  width: 1165px; 
  margin: auto;
}

.form-container h2 {
  text-align: center;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  grid-template-areas: 
    "description description"
    "date time"
    "tags tags"
    "amount amount"; 
}

.form-control {
  position: relative;
  width: 100%;
}

.form-control2 {
  position: relative;
  width: 100%;
}


.form-control:nth-child(1) {
  grid-area: description;
}

.form-control2:nth-child(2) {
  grid-area: date;
}

.form-control2:nth-child(3) {
  grid-area: time;
}

.form-control:nth-child(4) {
  grid-area: tags;
}

.amount-centered {
  grid-area: amount; 
  display: flex;
  justify-content: center;
}

.form-control input,
.form-control2 input {
  background-color: transparent;
  border: 1px solid #ccc;
  border-bottom: 2px #ccc solid;
  border-radius: 8px;
  display: block;
  width: 100%;
  padding: 15px 10px;
  font-size: 18px;
  color: #000000;
  margin-bottom: 20px;
  box-sizing: border-box;
}

.form-control input:focus,
.form-control2 input:focus,
.form-control input:valid,
.form-control2 input:valid {
  outline: 0;
  border-color: rgb(32, 180, 230);
}

.form-control label {
  position: absolute;
  top: 15px;
  left: 10px;
  pointer-events: none;
  display: flex;
}

.form-control label span,
.form-control2 label span {
  font-size: 18px;
  min-width: 5px;
  color: #615c5c;
  transition: 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.form-control input:focus+label span,
.form-control input:valid+label span {
  color: rgb(32, 180, 230);
  transform: translateY(-40px); 
}

button {
  position: relative;
  overflow: hidden;
  border: 1px solid #18181a;
  border-radius: 15px;
  color: #18181a;
  display: inline-block;
  font-size: 15px;
  line-height: 15px;
  padding: 15px 25px;
  text-decoration: none;
  cursor: pointer;
  background: #e8e8e8;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  z-index: 1;
  -webkit-box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
  box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
  font-weight: 1000;
}

button span:first-child {
  position: relative;
  transition: color 600ms cubic-bezier(0.48, 0, 0.12, 1);
  z-index: 10;
}

button span:last-child {
  color: white;
  display: block;
  position: absolute;
  bottom: 0;
  transition: all 500ms cubic-bezier(0.48, 0, 0.12, 1);
  z-index: 100;
  opacity: 0;
  top: 50%;
  left: 50%;
  transform: translateY(225%) translateX(-50%);
  height: 14px;
  line-height: 13px;
}

button:after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: black;
  transform-origin: bottom center;
  transition: transform 600ms cubic-bezier(0.48, 0, 0.12, 1);
  transform: scaleY(0);
  z-index: 50;
}

button:hover:after {
  transform-origin: bottom center;
  transform: scaleY(1);
}

button:hover span:last-child {
  transform: translateX(-50%) translateY(-50%);
  opacity: 1;
  transition: all 900ms cubic-bezier(0.48, 0, 0.12, 1);
}
</style>