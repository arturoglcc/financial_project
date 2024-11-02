<template>
    <div class="login-container">
      <div class="intro">
        <h1>Financial Organizer</h1>
        <p>
          This is a financial organizer that will help you keep track of your money,
          easily managing your financial transactions.
        </p>
      </div>
      <div class="login-form">
        <h2>Sign in</h2>
        <p>Log in by entering your email address and password.</p>
        <form @submit.prevent="handleLogin">
          <div class="input-group">
            <label for="email">Email address</label>
            <input type="email" id="email" v-model="email" required />
          </div>
          <div class="input-group">
            <label for="password">Password</label>
            <input type="password" id="password" v-model="password" required />
          </div>
          <button type="submit">Log in</button>
        </form>
        <a href="#">Forgot password?</a>
        <p>Don't have an account? <router-link to="/signup">Sign up</router-link></p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: '',
        password: ''
      };
    },
    methods: {
      handleLogin() {
        console.log('Email:', this.email, 'Password:', this.password);
      },
    },
  };
  </script>
  
  <style scoped>
  .login-container {
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
  
  .login-form {
    max-width: 300px;
    padding: 20px;
    background: #f5f5f5;
    border-radius: 8px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  }
  
  .login-form h2 {
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
  }
  
  .input-group input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    margin-top: 5px;
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
  
  a {
    display: block;
    color: #666;
    text-align: center;
    margin-top: 10px;
  }
  
  a:hover {
    color: #333;
  }
  </style>
  