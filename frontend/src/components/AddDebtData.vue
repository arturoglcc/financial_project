<template>
  <div class="form-container">
    <div class="button-container">
      <button class="top-button" @click="toggleForm(true)" :class="{ active: isFormA }">Add Debt</button>
      <button class="top-button" @click="toggleForm(false)" :class="{ active: !isFormA }">Add Purchase with credit</button>
    </div>
    <!-- Form Debt -->
    <form @submit.prevent="handleAdd" v-if="isFormA">
      <div class="form-grid">
        <div class="form-control">
          <input type="text" required v-model="description">
          <label>
            <span style="transition-delay:0ms">D</span><span style="transition-delay:50ms">e</span><span style="transition-delay:100ms">s</span><span style="transition-delay:150ms">c</span><span style="transition-delay:200ms">r</span><span style="transition-delay:250ms">i</span><span style="transition-delay:300ms">p</span><span style="transition-delay:350ms">t</span><span style="transition-delay:400ms">i</span><span style="transition-delay:450ms">o</span><span style="transition-delay:500ms">n</span>
          </label>
        </div>
        <div class="form-control2">
          <label for="dateInput">Date</label>
          <input class="input-date-time" type="date" id="dateInput" v-model="dateInput" required />
        </div>
        <div class="form-control2">
          <label for="timeInput">Time</label>
          <input class="input-date-time" type="time" id="timeInput" v-model="timeInput" required />
        </div>
        <div class="form-control">
          <input type="text" required v-model="creditor">
          <label>
            <span style="transition-delay:0ms">C</span><span style="transition-delay:50ms">r</span><span style="transition-delay:100ms">e</span><span style="transition-delay:150ms">d</span><span style="transition-delay:200ms">i</span><span style="transition-delay:250ms">t</span><span style="transition-delay:300ms">o</span><span style="transition-delay:350ms">r</span>
          </label>
        </div>
        <div class="form-control amount-centered">
          <input type="float" required v-model="amount">
          <label>
            <span style="transition-delay:0ms">A</span><span style="transition-delay:50ms">m</span><span style="transition-delay:100ms">o</span><span style="transition-delay:150ms">u</span><span style="transition-delay:200ms">n</span><span style="transition-delay:250ms">t</span><span style="transition-delay:300ms"> </span><span style="transition-delay:350ms">$</span>
          </label>
        </div>
        <small>*Set the time in 24 hour format, for example, 22:15 <br> *Enter the amount with two decimal numbers, for example: 100.00</small>
        <button class="button" @click="handleConfirm"><span class="text">Confirm</span><span>Confirm</span></button>
      </div>
    </form>
    <!-- Form Credit -->
    <form @submit.prevent="handleAddCredit" v-else>
      <div class="form-grid">
        <div class="form-control">
          <input type="text" required v-model="descriptionCredit">
          <label>
            <span style="transition-delay:0ms">D</span><span style="transition-delay:50ms">e</span><span style="transition-delay:100ms">s</span><span style="transition-delay:150ms">c</span><span style="transition-delay:200ms">r</span><span style="transition-delay:250ms">i</span><span style="transition-delay:300ms">p</span><span style="transition-delay:350ms">t</span><span style="transition-delay:400ms">i</span><span style="transition-delay:450ms">o</span><span style="transition-delay:500ms">n</span>
          </label>
        </div>
        <div class="form-control2">
          <label for="dateInputCredit">Date</label>
          <input class="input-date-time" type="date" id="dateInputCredit" v-model="dateInputCredit" required />
        </div>
        <div class="form-control2">
          <label for="timeInputCredit">Time</label>
          <input class="input-date-time" type="time" id="timeInputCredit" v-model="timeInputCredit" required />
        </div>
        <div class="form-control amount-centered">
          <input type="float" required v-model="amountCredit">
          <label>
            <span style="transition-delay:0ms">A</span><span style="transition-delay:50ms">m</span><span style="transition-delay:100ms">o</span><span style="transition-delay:150ms">u</span><span style="transition-delay:200ms">n</span><span style="transition-delay:250ms">t</span><span style="transition-delay:300ms"> </span><span style="transition-delay:350ms">$</span>
          </label>
        </div>
        <div class="form-control checkbox-control">
          <input type="checkbox" id="interestFreeCheckbox" v-model="isInterestFree" />
          <label for="interestFreeCheckbox">Interest-free months</label>
        </div>
        <div class="form-control">
          <input type="number" min="0" required v-model="interestCredit" :disabled="!isInterestFree">
          <label>
            <span style="transition-delay:0ms">I</span><span style="transition-delay:50ms">n</span><span style="transition-delay:100ms">t</span><span style="transition-delay:150ms">e</span><span style="transition-delay:200ms">r</span><span style="transition-delay:250ms">e</span><span style="transition-delay:300ms">s</span><span style="transition-delay:350ms">t</span><span style="transition-delay:400ms">-</span><span style="transition-delay:450ms">f</span><span style="transition-delay:500ms">r</span><span style="transition-delay:550ms">e</span><span style="transition-delay:600ms">e</span><span style="transition-delay:700ms">m</span><span style="transition-delay:750ms">o</span><span style="transition-delay:800ms">n</span><span style="transition-delay:850ms">t</span><span style="transition-delay:900ms">h</span><span style="transition-delay:950ms">s</span>
          </label>
        </div>
        <small>*Set the time in 24 hour format, for example, 22:15 <br> *Enter the amount with two decimal numbers, for example: 100.00</small>
        <button class="button" @click="handleConfirmCredit"><span class="text">Confirm</span><span>Confirm</span></button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isFormA: true,
      isInterestFree: false,
      description: "",
      dateInput: "",
      timeInput: "",
      creditor: "",
      amount: "",
      descriptionCredit: "",
      dateInputCredit: "",
      timeInputCredit: "",
      interestCredit: "",
      amountCredit: "",
    };
  },
  methods: {
    toggleForm(isFormA) {
      this.isFormA = isFormA;
    },
    handleConfirm() {
      this.description = "";
      this.dateInput = "";
      this.creditor = "";
      this.timeInput = "";
      this.amount = "";
    },
    handleConfirmCredit() {
      this.descriptionCredit = "";
      this.dateInputCredit = "";
      this.interestCredit = "";
      this.timeInputCredit = "";
      this.amountCredit = "";
      this.isInterestFree = false;
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

.button-container {
  display:flex;
  justify-content:center;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
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

.form-control.checkbox-control {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 10px;
  font-size: 18px;
  color: #615c5c;
}

.form-control.checkbox-control input[type="checkbox"] {
  width: 20px;
  height: 20px;
  cursor: pointer;
}

.form-control.checkbox-control label {
  cursor: pointer;
  font-weight: 500;
  line-height: 20px;
}

.form-control input[type="number"]:disabled {
  background-color: #f0f0f0;
  color: #a0a0a0;
  cursor: not-allowed;
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

.button {
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

.button span:first-child {
  position: relative;
  transition: color 600ms cubic-bezier(0.48, 0, 0.12, 1);
  z-index: 10;
}

.button span:last-child {
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

.button:after {
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

.button:hover:after {
  transform-origin: bottom center;
  transform: scaleY(1);
}

.button:hover span:last-child {
  transform: translateX(-50%) translateY(-50%);
  opacity: 1;
  transition: all 900ms cubic-bezier(0.48, 0, 0.12, 1);
}

.top-button {
  flex: 1;
  padding: 10px;
  text-align: center;
  font-weight: 600;
  color: #615c5c;
  background-color: transparent;
  border: none;
  cursor: pointer;
  margin-bottom: 1.5rem;
  transition: color 0.3s ease, border-bottom 0.3s ease;
}

.top-button:hover {
  color: rgb(32, 180, 230);
}

.top-button.active {
  color: #18181a;
  border-bottom: 2px solid rgb(32, 180, 230);
}

</style>