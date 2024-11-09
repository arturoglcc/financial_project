<template>
  <div class="sidebar" :class="{ 'sidebarExpanded': menuOpen }">
    <button class="hamburger" @click="toggleMenu">
      <div class="hamburgerIcon">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </button>
    <nav class="navMenu">
      <router-link to="/home" class="navItem">
        <svg xmlns="http://www.w3.org/2000/svg" class="navIcon" width="24" height="24" viewBox="0 0 24 24">
          <path fill="currentColor" d="M10 20v-6h4v6h5v-8h3L12 3L2 12h3v8z" />
        </svg>
        <span class="navText" :class="{ 'showText': menuOpen }">Home</span>
      </router-link>
      <router-link to="/user-settings" class="navItem">
        <svg xmlns="http://www.w3.org/2000/svg" class="navIcon" width="24" height="24" viewBox="0 0 24 24">
          <path fill="currentColor" d="M10 3.5C8.563 3.5 7.42 4.631 7.42 6S8.564 8.5 10 8.5s2.579-1.131 2.579-2.5s-1.143-2.5-2.58-2.5M6.42 6c0-1.945 1.615-3.5 3.58-3.5c1.964 0 3.579 1.555 3.579 3.5s-1.615 3.5-3.58 3.5C8.036 9.5 6.422 7.945 6.422 6m1.186 5.756c-.218-.14-.43-.18-.585-.138q-.22.06-.439.13l-.984.316a2.52 2.52 0 0 0-1.629 1.56c-.03.09-.05.194-.064.327l-.39 3.695l-.001.009c-.09.636.252 1.175.824 1.308c1.097.254 2.93.537 5.662.537a.5.5 0 0 1 0 1c-2.8 0-4.71-.29-5.888-.563c-1.147-.266-1.737-1.345-1.59-2.414l.389-3.677c.017-.164.046-.355.113-.549a3.52 3.52 0 0 1 2.269-2.185l.984-.316q.238-.076.478-.142c.52-.143 1.028.026 1.394.263c.394.254 1.045.569 1.85.569s1.457-.315 1.851-.57c.367-.236.874-.405 1.394-.262q.24.067.478.142l.985.316a.5.5 0 1 1-.305.952l-.985-.315q-.217-.07-.438-.13c-.156-.043-.367-.004-.586.137c-.489.317-1.329.73-2.393.73c-1.065 0-1.905-.413-2.394-.73" />
          <path fill="currentColor" d="M15.64 13.16a.73.73 0 0 1 .731-.66h1.257a.73.73 0 0 1 .732.66c.018.207.177.428.463.574q.084.043.167.09c.314.18.621.213.843.114a.74.74 0 0 1 .934.286l.628 1.032a.715.715 0 0 1-.221.971c-.18.118-.303.378-.299.725v.096c-.005.347.12.607.299.725a.715.715 0 0 1 .221.971l-.628 1.032a.74.74 0 0 1-.934.286c-.222-.099-.529-.066-.843.114q-.082.046-.167.09c-.286.146-.445.367-.463.574a.73.73 0 0 1-.732.66H16.37a.73.73 0 0 1-.731-.66c-.019-.207-.178-.428-.464-.574a4 4 0 0 1-.166-.09c-.315-.18-.622-.213-.844-.114a.74.74 0 0 1-.934-.286l-.628-1.032a.715.715 0 0 1 .222-.971c.18-.118.303-.378.298-.725v-.096c.005-.347-.119-.607-.298-.725a.715.715 0 0 1-.222-.971l.628-1.032a.74.74 0 0 1 .934-.286c.222.099.53.066.844-.114q.082-.046.166-.09c.286-.146.445-.367.464-.574m.952.34c-.138.526-.541.911-.962 1.125l-.124.067c-.424.243-.984.395-1.532.237l-.385.632c.401.382.541.934.535 1.404v.07c.006.47-.134 1.022-.535 1.404l.385.632c.548-.158 1.108-.006 1.532.237q.06.034.124.067c.42.214.824.6.962 1.125h.815c.138-.526.542-.911.962-1.125l.124-.067c.424-.243.985-.395 1.533-.237l.384-.632c-.401-.382-.541-.934-.535-1.404v-.07c-.006-.47.134-1.022.535-1.404l-.384-.632c-.549.158-1.109.006-1.533-.237l-.124-.067c-.42-.214-.824-.6-.962-1.125zm1.199 3.093c-.244-.4-.806-.555-1.255-.31c-.434.239-.56.74-.328 1.124c.244.4.806.555 1.255.31c.434-.239.56-.74.328-1.124m-1.735-1.186c.897-.491 2.055-.21 2.589.666c.544.893.209 2.022-.702 2.52c-.897.491-2.055.21-2.589-.666c-.543-.893-.209-2.022.702-2.52" />
        </svg>
        <span class="navText" :class="{ 'showText': menuOpen }">User settings</span>
      </router-link>
      <router-link to="/change-password" class="navItem">
        <svg xmlns="http://www.w3.org/2000/svg" class="navIcon" width="24" height="24" viewBox="0 0 24 24">
          <path fill="currentColor" d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12c5.16-1.26 9-6.45 9-12V5zm0 6c1.4 0 2.8 1.1 2.8 2.5V11c.6 0 1.2.6 1.2 1.3v3.5c0 .6-.6 1.2-1.3 1.2H9.2c-.6 0-1.2-.6-1.2-1.3v-3.5c0-.6.6-1.2 1.2-1.2V9.5C9.2 8.1 10.6 7 12 7m0 1.2c-.8 0-1.5.5-1.5 1.3V11h3V9.5c0-.8-.7-1.3-1.5-1.3" />
        </svg>
        <span class="navText" :class="{ 'showText': menuOpen }">Change password</span>
      </router-link>
      <a href="#" class="navItem">
        <svg xmlns="http://www.w3.org/2000/svg" class="navIcon" width="24" height="24" viewBox="0 0 24 24">
          <path fill="currentColor" d="M13 3a9 9 0 0 0-9 9H1l3.89 3.89l.07.14L9 12H6c0-3.87 3.13-7 7-7s7 3.13 7 7s-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06l-1.42 1.42A8.95 8.95 0 0 0 13 21a9 9 0 0 0 0-18m-1 5v5l4.25 2.52l.77-1.28l-3.52-2.09V8z" />
        </svg>
        <span class="navText" :class="{ 'showText': menuOpen }">History movements</span>
      </a>
      <a href="#" class="navItem">
        <svg xmlns="http://www.w3.org/2000/svg" class="navIcon" width="24" height="24" viewBox="0 0 16 16">
          <path fill="currentColor" fill-rule="evenodd" d="M0 0h1v15h15v1H0zm10 3.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-1 0V4.9l-3.613 4.417a.5.5 0 0 1-.74.037L7.06 6.767l-3.656 5.027a.5.5 0 0 1-.808-.588l4-5.5a.5.5 0 0 1 .758-.06l2.609 2.61L13.445 4H10.5a.5.5 0 0 1-.5-.5" />
        </svg>
        <span class="navText" :class="{ 'showText': menuOpen }">Graphs</span>
      </a>
      <a href="#" class="navItem" @click="handleLogout">
        <svg xmlns="http://www.w3.org/2000/svg" class="navIcon" width="24" height="24" viewBox="0 0 24 24">
          <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
            <path stroke-dasharray="36" stroke-dashoffset="36" d="M12 4h-7c-0.55 0 -1 0.45 -1 1v14c0 0.55 0.45 1 1 1h7">
              <animate fill="freeze" attributeName="stroke-dashoffset" dur="0.5s" values="36;0" />
            </path>
            <path stroke-dasharray="14" stroke-dashoffset="14" d="M9 12h11.5">
              <animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s" values="14;0" />
            </path>
            <path stroke-dasharray="6" stroke-dashoffset="6" d="M20.5 12l-3.5 -3.5M20.5 12l-3.5 3.5">
              <animate fill="freeze" attributeName="stroke-dashoffset" begin="0.8s" dur="0.2s" values="6;0" />
            </path>
          </g>
        </svg>
        <span class="navText" :class="{ 'showText': menuOpen }">Log out</span>
      </a>
      <a href="https://github.com/arturoglcc/financial_project/" target="_blank" class="navItem mtAuto">
        <svg xmlns="http://www.w3.org/2000/svg" class="navIcon" width="24" height="24" viewBox="0 0 16 16">
          <path fill="currentColor" fill-rule="evenodd" d="M7.5.25a7.25 7.25 0 0 0-2.292 14.13c.363.066.495-.158.495-.35c0-.172-.006-.628-.01-1.233c-2.016.438-2.442-.972-2.442-.972c-.33-.838-.805-1.06-.805-1.06c-.658-.45.05-.441.05-.441c.728.051 1.11.747 1.11.747c.647 1.108 1.697.788 2.11.602c.066-.468.254-.788.46-.969c-1.61-.183-3.302-.805-3.302-3.583a2.8 2.8 0 0 1 .747-1.945c-.075-.184-.324-.92.07-1.92c0 0 .61-.194 1.994.744A7 7 0 0 1 7.5 3.756A7 7 0 0 1 9.315 4c1.384-.938 1.992-.743 1.992-.743c.396.998.147 1.735.072 1.919c.465.507.745 1.153.745 1.945c0 2.785-1.695 3.398-3.31 3.577c.26.224.492.667.492 1.343c0 .97-.009 1.751-.009 1.989c0 .194.131.42.499.349A7.25 7.25 0 0 0 7.499.25" clip-rule="evenodd" />
        </svg>
        <span class="navText" :class="{ 'showText': menuOpen }">Project</span>
      </a>
    </nav>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        menuOpen: false,
      };
    },
    methods: {
      toggleMenu() {
        this.menuOpen = !this.menuOpen;
      },
      async handleLogout() {
      try {
        const response = await fetch('http://localhost/api/logout', {
          method: 'POST', // Adjust method as needed (POST/GET)
          credentials: 'include',
        });
        if (response.ok) {
          console.log('Logout successful');
          // Redirect to login page or home page
          this.$router.push('/');
        } else {
          console.error('Logout failed:', response.statusText);
        }
      } catch (error) {
        console.error('Error during logout:', error);
      }
    },
  },
};
</script>

<style scoped>
.sidebar {
  background-color: #EBEBEB;
  width: 60px;
  transition: width 0.3s ease;
  padding: 1rem 0;
  display: flex;
  flex-direction: column;
  position: fixed;
  height: 100%;
  z-index: 100;
}

.sidebarExpanded {
  width: 240px;
}

.hamburger {
  background: none;
  border: none;
  padding: 0.5rem;
  margin: 0 0.5rem 1rem;
  cursor: pointer;
}

.hamburgerIcon {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.hamburgerIcon span {
  display: block;
  width: 24px;
  height: 2px;
  background-color: #333;
  transition: all 0.3s ease;
}

.navMenu {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  flex-grow: 1;
}

.navItem {
  display: flex;
  align-items: center;
  padding: 0.75rem 1rem;
  text-decoration: none;
  color: #333;
  transition: background-color 0.2s ease;
}

.navItem:hover {
  background-color: #e5e5e5;
}

.navIcon {
  width: 24px;
  height: 24px;
  margin-right: 1rem;
  flex-shrink: 0;
}

.navText {
  opacity: 0;
  transition: opacity 0.2s ease;
  white-space: nowrap;
}

.showText {
  opacity: 1;
}

.mtAuto {
  margin-top: auto;
  margin-bottom: 2rem;
}
</style>