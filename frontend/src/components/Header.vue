<template>
  <header class="header">
    <button class="menuToggle" @click="$emit('toggle-menu')">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
        <path d="M3 12h18v2H3zM3 6h18v2H3zm0 12h18v2H3z"/>
      </svg>
    </button>
    <h1 class="headerTitle">Financial Organizer</h1>
    <div class="userInfo">
      <span>{{ username }}</span>
      <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
        <path fill="currentColor" fill-opacity="0.25" d="M3 12a9 9 0 1 1 18 0a9 9 0 0 1-18 0" />
        <circle cx="12" cy="10" r="4" fill="currentColor" />
        <path fill="currentColor" fill-rule="evenodd" d="M18.22 18.246c.06.097.041.22-.04.297A8.97 8.97 0 0 1 12 21a8.97 8.97 0 0 1-6.18-2.457a.24.24 0 0 1-.04-.297C6.942 16.318 9.291 15 12 15s5.057 1.318 6.22 3.246" clip-rule="evenodd" />
      </svg>
    </div>
  </header>
</template>

<script>
export default {
  data() {
    return {
      username: 'Loading...', // Default placeholder while fetching the username
    };
  },
  async created() {
    // Make the API call when the component is created
    try {
      const response = await fetch('http://localhost/api/me', {
        method: 'GET',
        credentials: 'include', // Include cookies in the request
      });
      if (response.ok) {
        const data = await response.json();
        this.username = data.username || 'Unknown User'; // Fallback if username is not returned
      } else {
        console.error('Failed to fetch user info:', response.statusText);
        this.username = 'Guest'; // Fallback if the request fails
      }
    } catch (error) {
      console.error('Error fetching user info:', error);
      this.username = 'Guest'; // Fallback in case of an error
    }
  },
};
</script>


<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  display: flex;
  align-items: center;
  padding: 0 1rem;
  background-color: #F7F6F6;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 99;
}

.menuToggle {
  background: none;
  border: none;
  cursor: pointer;
  margin-right: 1rem;
}

.headerTitle {
  flex-grow: 1;
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
  text-align: center;
}

.userInfo {
  display: flex;
  align-items: center;
}

.userInfo svg {
  margin-left: 1rem;
  width: 45px;
  height: 45px;
}
</style>
