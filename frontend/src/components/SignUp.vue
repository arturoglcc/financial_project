<template>
  <div class="signup-container">
    <div class="intro">
      <h1>Financial Organizer</h1>
      <p>
        This is a financial organizer that will help you keep track of your
        money, easily managing your financial transactions.
      </p>
    </div>
    <div class="signup-form">
      <h2>Create Your Account</h2>

      <div v-if="successMessage" class="success-message">{{ successMessage }}</div>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>

      
      <form @submit.prevent="handleSignUp">
        <div class="input-group">
          <label for="username">Username</label>
          <div class="input-container group">
            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" class="icon">
              <path fill="none" stroke="currentColor" d="M18.5 20.247V16S16 14.5 12 14.5S5.5 16 5.5 16v4.247M1.5 12C1.5 6.201 6.201 1.5 12 1.5S22.5 6.201 22.5 12S17.799 22.5 12 22.5S1.5 17.799 1.5 12Zm10.426.5S8.5 10.68 8.5 8c0-1.933 1.569-3.5 3.504-3.5A3.495 3.495 0 0 1 15.5 8c0 2.68-3.426 4.5-3.426 4.5z" />
            </svg>
            <input type="text" id="username" v-model="username" @input="clearErrorMessage" required class="input" />
          </div>
        </div>
        <div class="input-group">
          <label for="email">Email address</label>
          <div class="input-container group">
            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 16 16" class="icon">
              <path fill="currentColor" fill-rule="evenodd" d="M14.95 3.684L8.637 8.912a1 1 0 0 1-1.276 0l-6.31-5.228A1 1 0 0 0 1 4v8a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4a1 1 0 0 0-.05-.316M2 2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2m-.21 1l5.576 4.603a1 1 0 0 0 1.27.003L14.268 3z"/>
            </svg>
            <input type="email" id="email" v-model="email" @input="clearErrorMessage" required class="input" />
          </div>
        </div>
        <div class="input-group">
          <label for="password">Password</label>
          <div class="input-container group">
            <svg stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="icon">
              <path d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" stroke-linejoin="round" stroke-linecap="round"></path>
            </svg>
            <input :type="showPassword ? 'text' : 'password'" id="password" v-model="password" @input="clearErrorMessage" required class="input" />
            <svg class="input-icon clickable" viewBox="0 0 24 24" @click="togglePassword">
              <path v-if="showPassword" d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zm0 12c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z" />
              <path v-else d="M12 7c2.76 0 5 2.24 5 5 0 .65-.13 1.26-.36 1.83l2.92 2.92c1.51-1.26 2.7-2.89 3.43-4.75-1.73-4.39-6-7.5-11-7.5-1.4 0-2.74.25-3.98.7l2.16 2.16C10.74 7.13 11.35 7 12 7zM2 4.27l2.28 2.28.46.46C3.08 8.3 1.78 10.02 1 12c1.73 4.39 6 7.5 11 7.5 1.55 0 3.03-.3 4.38-.84l.42.42L19.73 22 21 20.73 3.27 3 2 4.27zM7.53 9.8l1.55 1.55c-.05.21-.08.43-.08.65 0 1.66 1.34 3 3 3 .22 0 .44-.03.65-.08l1.55 1.55c-.67.33-1.41.53-2.2.53-2.76 0-5-2.24-5-5 0-.79.2-1.53.53-2.2zm4.31-.78l3.15 3.15.02-.16c0-1.66-1.34-3-3-3l-.17.01z" />
            </svg>
          </div>
        </div>
        <div class="input-group">
          <label for="confirm-password">Confirm Password</label>
          <div class="input-container group">
            <svg stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="icon">
              <path d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" stroke-linejoin="round" stroke-linecap="round"></path>
            </svg>
            <input :type="showPassword2 ? 'text' : 'password'" id="confirm-password" v-model="confirmPassword" @input="clearErrorMessage" required class="input" />
            <svg class="input-icon clickable" viewBox="0 0 24 24" @click="toggleConfirmPassword">
              <path v-if="showPassword2" d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zm0 12c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z" />
              <path v-else d="M12 7c2.76 0 5 2.24 5 5 0 .65-.13 1.26-.36 1.83l2.92 2.92c1.51-1.26 2.7-2.89 3.43-4.75-1.73-4.39-6-7.5-11-7.5-1.4 0-2.74.25-3.98.7l2.16 2.16C10.74 7.13 11.35 7 12 7zM2 4.27l2.28 2.28.46.46C3.08 8.3 1.78 10.02 1 12c1.73 4.39 6 7.5 11 7.5 1.55 0 3.03-.3 4.38-.84l.42.42L19.73 22 21 20.73 3.27 3 2 4.27zM7.53 9.8l1.55 1.55c-.05.21-.08.43-.08.65 0 1.66 1.34 3 3 3 .22 0 .44-.03.65-.08l1.55 1.55c-.67.33-1.41.53-2.2.53-2.76 0-5-2.24-5-5 0-.79.2-1.53.53-2.2zm4.31-.78l3.15 3.15.02-.16c0-1.66-1.34-3-3-3l-.17.01z" />
            </svg>
          </div>
        </div>
        <button type="submit">Create Account</button>
      </form>
      <p>
        By creating an account, you agree to the Terms of Service and Privacy
        Policy.
      </p>
      <p class="signup-text">Already have an account? <router-link to="/">Log in</router-link></p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
      showPassword: false,
      showPassword2: false,
      successMessage: "",
      errorMessage: ""
    };
  },
  methods: {
    async handleSignUp() {
      // Log both passwords for troubleshooting
      console.log("Password:", this.password, "Confirm Password:", this.confirmPassword);
      if (this.password !== this.confirmPassword) {
        this.errorMessage = "Passwords do not match.";
        this.username = "";
        this.email = "";
        this.password = "";
        this.confirmPassword = "";
        return;
      }
      try {
        // Send the data to the server with a POST request using fetch
        const response = await fetch("http://localhost/api/signup", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            username: this.username,
            email: this.email,
            password: this.password 
          })
        });

        // Check if the request was successful
        if (response.ok) {
          const result = await response.json();
          this.successMessage = "Sign-up successful! Welcome, " + result.user.username;
          console.log("Sign-up successful:", result);
          this.$router.push("/home");
        } else {
          const errorMessage = await response.text();
          this.errorMessage = "Sign-up failed: " + errorMessage;
          console.error("Sign-up failed:", errorMessage);
          this.username = "";
          this.email = "";
          this.password = "";
          this.confirmPassword = "";
        }
      } catch (error) {
        console.error("Error connecting to server:", error);
        alert("An error occurred while signing up. Please try again later.");
        this.username = "";
        this.email = "";
        this.password = "";
        this.confirmPassword = "";
      }
    },

    togglePassword() {
      this.showPassword = !this.showPassword;
    },
    toggleConfirmPassword() {
      this.showPassword2 = !this.showPassword2;
    },
    clearErrorMessage() {
      this.errorMessage = "";
    },
  }
};
</script>


<style scoped>
.signup-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-family: Arial, sans-serif;
}

.intro {
  max-width: 300px;
  padding: 20px;
  text-align: center;
}

.intro h1 {
  font-size: 2em;
  font-weight: bold;
}

.intro p {
  font-size: 1em;
  color: #666;
}

.signup-form {
  max-width: 300px;
  padding: 20px;
  background: #f5f5f5;
  border-radius: 15px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.signup-form h2 {
  font-size: 1.5em;
  font-weight: bold;
}

.input-group {
  margin: 15px 0;
}

.input-group label {
  display: block;
  font-size: 0.9em;
  color: #333;
  margin-bottom: 6px;
}

.input-container {
  position: relative;
}

.group {
  display: flex;
  line-height: 30px;
  align-items: center;
  position: relative;
}

.input {
  width: 100%;
  height: 45px;
  line-height: 30px;
  padding: 0 5rem;
  padding-left: 3rem;
  border: 1px solid #ddd;
  border-radius: 10px;
  outline: none;
  background-color: #f8fafc;
  color: #0d0c22;
  transition: .5s ease;
}

.input::placeholder {
  color: #94a3b8;
}

.input:focus, .input:hover {
  outline: none;
  border-color: rgba(129, 140, 248);
  background-color: #fff;
  box-shadow: 0 0 0 5px rgb(129 140 248 / 30%);
}

.icon {
  position: absolute;
  left: 1rem;
  fill: none;
  width: 1rem;
  height: 1rem;
}

.input-icon {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 20px;
  fill: #666;
  cursor: pointer;
}

button {
  width: 100%;
  padding: 10px;
  background: black;
  color: white;
  font-size: 1em;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 10px;
}

button:hover {
  background: #333;
}

p {
  color: #666;
  text-align: center;
  margin-top: 10px;
  margin-bottom: 10px;
}

.signup-text {
  text-align: center;
  color: #666;
  margin: 0;
}

.signup-text a {
  text-decoration: none;
}

.signup-text a:hover {
  text-decoration: underline;
}

.success-message {
  color: green;
  font-size: 0.9em;
  margin-bottom: 10px;
  text-align: center;
}

.error-message {
  color: red;
  font-size: 0.9em;
  margin-bottom: 10px;
  text-align: center;
}

</style>
