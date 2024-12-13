<template>
  <div class="adds-container">
    <router-link to="/add-income" class="add-card light">
      <div class="add-title">
        Add <br> income
      </div>
      <div class="add-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
          <mask id="lineMdPlusSquareFilled0">
            <g fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
              <path fill="#fff" fill-opacity="0" stroke-dasharray="64" stroke-dashoffset="64"
                d="M4 12v-7c0 -0.55 0.45 -1 1 -1h14c0.55 0 1 0.45 1 1v14c0 0.55 -0.45 1 -1 1h-14c-0.55 0 -1 -0.45 -1 -1Z">
                <animate fill="freeze" attributeName="fill-opacity" begin="0.6s" dur="0.5s" values="0;1" />
                <animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="64;0" />
              </path>
              <path stroke="#000" stroke-dasharray="12" stroke-dashoffset="12" d="M7 12h10">
                <animate fill="freeze" attributeName="stroke-dashoffset" begin="1.1s" dur="0.2s" values="12;0" />
              </path>
              <path stroke="#000" stroke-dasharray="12" stroke-dashoffset="12" d="M12 7v10">
                <animate fill="freeze" attributeName="stroke-dashoffset" begin="1.3s" dur="0.2s" values="12;0" />
              </path>
            </g>
          </mask>
          <rect width="24" height="24" fill="currentColor" mask="url(#lineMdPlusSquareFilled0)" />
        </svg>
      </div>
    </router-link>
    <router-link to="/add-outlay" class="add-card dark">
      <div class="add-title">
        Add <br> outlay
      </div>
      <div class="add-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
          <mask id="lineMdPlusSquareFilled0">
            <g fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
              <path fill="#fff" fill-opacity="0" stroke-dasharray="64" stroke-dashoffset="64"
                d="M4 12v-7c0 -0.55 0.45 -1 1 -1h14c0.55 0 1 0.45 1 1v14c0 0.55 -0.45 1 -1 1h-14c-0.55 0 -1 -0.45 -1 -1Z">
                <animate fill="freeze" attributeName="fill-opacity" begin="0.6s" dur="0.5s" values="0;1" />
                <animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="64;0" />
              </path>
              <path stroke="#000" stroke-dasharray="12" stroke-dashoffset="12" d="M7 12h10">
                <animate fill="freeze" attributeName="stroke-dashoffset" begin="1.1s" dur="0.2s" values="12;0" />
              </path>
              <path stroke="#000" stroke-dasharray="12" stroke-dashoffset="12" d="M12 7v10">
                <animate fill="freeze" attributeName="stroke-dashoffset" begin="1.3s" dur="0.2s" values="12;0" />
              </path>
            </g>
          </mask>
          <rect width="24" height="24" fill="currentColor" mask="url(#lineMdPlusSquareFilled0)" />
        </svg>
      </div>
    </router-link>
    <router-link to="/add-debt" class="add-card light">
      <div class="add-title">
        Add <br> debt
      </div>
      <div class="add-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
          <mask id="lineMdPlusSquareFilled0">
            <g fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
              <path fill="#fff" fill-opacity="0" stroke-dasharray="64" stroke-dashoffset="64"
                d="M4 12v-7c0 -0.55 0.45 -1 1 -1h14c0.55 0 1 0.45 1 1v14c0 0.55 -0.45 1 -1 1h-14c-0.55 0 -1 -0.45 -1 -1Z">
                <animate fill="freeze" attributeName="fill-opacity" begin="0.6s" dur="0.5s" values="0;1" />
                <animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s" values="64;0" />
              </path>
              <path stroke="#000" stroke-dasharray="12" stroke-dashoffset="12" d="M7 12h10">
                <animate fill="freeze" attributeName="stroke-dashoffset" begin="1.1s" dur="0.2s" values="12;0" />
              </path>
              <path stroke="#000" stroke-dasharray="12" stroke-dashoffset="12" d="M12 7v10">
                <animate fill="freeze" attributeName="stroke-dashoffset" begin="1.3s" dur="0.2s" values="12;0" />
              </path>
            </g>
          </mask>
          <rect width="24" height="24" fill="currentColor" mask="url(#lineMdPlusSquareFilled0)" />
        </svg>
      </div>
    </router-link>
  </div>
</template>

<style scoped>
.adds-container {
  display: flex;
  justify-content: center;
  gap: 156px;
}

.add-card {
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 15px;
  width: 250px;
  height: 100px;
  text-align: left;
  position: relative;
  text-decoration: none;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.add-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
}

.add-card.dark {
  background-color: #333;
  color: white;
}

.add-card.light {
  background-color: white;
  color: #333;
}

.add-title {
  font-weight: bold;
  font-size: 28px;
  margin-left: 15px;
  transform: translateY(3%);
}

.add-icon {
  position: absolute;
  top: 15px;
  right: 23px;
  font-size: 2.5em;
}
</style>