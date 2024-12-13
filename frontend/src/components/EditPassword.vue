<template>
  <div class="edit-form">
    <h2>Edit password</h2>
    <form @submit.prevent="confirmEdit">
      <div class="input-group">
        <label for="password">Password</label>
        <div class="input-container group">
          <svg stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"
            class="icon">
            <path
              d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z"
              stroke-linejoin="round" stroke-linecap="round"></path>
          </svg>
          <input :type="showPassword ? 'text' : 'password'" id="password" v-model="password" :disabled="!isEditing"
            class="input" />
          <svg class="input-icon clickable" viewBox="0 0 24 24" @click="togglePassword">
            <path v-if="showPassword"
              d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zm0 12c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z" />
            <path v-else
              d="M12 7c2.76 0 5 2.24 5 5 0 .65-.13 1.26-.36 1.83l2.92 2.92c1.51-1.26 2.7-2.89 3.43-4.75-1.73-4.39-6-7.5-11-7.5-1.4 0-2.74.25-3.98.7l2.16 2.16C10.74 7.13 11.35 7 12 7zM2 4.27l2.28 2.28.46.46C3.08 8.3 1.78 10.02 1 12c1.73 4.39 6 7.5 11 7.5 1.55 0 3.03-.3 4.38-.84l.42.42L19.73 22 21 20.73 3.27 3 2 4.27zM7.53 9.8l1.55 1.55c-.05.21-.08.43-.08.65 0 1.66 1.34 3 3 3 .22 0 .44-.03.65-.08l1.55 1.55c-.67.33-1.41.53-2.2.53-2.76 0-5-2.24-5-5 0-.79.2-1.53.53-2.2zm4.31-.78l3.15 3.15.02-.16c0-1.66-1.34-3-3-3l-.17.01z" />
          </svg>
        </div>
      </div>
      <div class="input-group">
        <label for="new-password">New password</label>
        <div class="input-container group">
          <svg stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"
            class="icon">
            <path
              d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z"
              stroke-linejoin="round" stroke-linecap="round"></path>
          </svg>
          <input :type="showPassword2 ? 'text' : 'password'" id="new-password" v-model="newPassword"
            :disabled="!isEditing" class="input" />
          <svg class="input-icon clickable" viewBox="0 0 24 24" @click="toggleNewPassword">
            <path v-if="showPassword2"
              d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zm0 12c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z" />
            <path v-else
              d="M12 7c2.76 0 5 2.24 5 5 0 .65-.13 1.26-.36 1.83l2.92 2.92c1.51-1.26 2.7-2.89 3.43-4.75-1.73-4.39-6-7.5-11-7.5-1.4 0-2.74.25-3.98.7l2.16 2.16C10.74 7.13 11.35 7 12 7zM2 4.27l2.28 2.28.46.46C3.08 8.3 1.78 10.02 1 12c1.73 4.39 6 7.5 11 7.5 1.55 0 3.03-.3 4.38-.84l.42.42L19.73 22 21 20.73 3.27 3 2 4.27zM7.53 9.8l1.55 1.55c-.05.21-.08.43-.08.65 0 1.66 1.34 3 3 3 .22 0 .44-.03.65-.08l1.55 1.55c-.67.33-1.41.53-2.2.53-2.76 0-5-2.24-5-5 0-.79.2-1.53.53-2.2zm4.31-.78l3.15 3.15.02-.16c0-1.66-1.34-3-3-3l-.17.01z" />
          </svg>
        </div>
      </div>
      <div class="input-group">
        <label for="confirm-password">Confirm new password</label>
        <div class="input-container group">
          <svg stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"
            class="icon">
            <path
              d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z"
              stroke-linejoin="round" stroke-linecap="round"></path>
          </svg>
          <input :type="showPassword3 ? 'text' : 'password'" id="confirm-password" v-model="confirmPassword"
            :disabled="!isEditing" class="input" />
          <svg class="input-icon clickable" viewBox="0 0 24 24" @click="toggleConfirmPassword">
            <path v-if="showPassword3"
              d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zm0 12c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z" />
            <path v-else
              d="M12 7c2.76 0 5 2.24 5 5 0 .65-.13 1.26-.36 1.83l2.92 2.92c1.51-1.26 2.7-2.89 3.43-4.75-1.73-4.39-6-7.5-11-7.5-1.4 0-2.74.25-3.98.7l2.16 2.16C10.74 7.13 11.35 7 12 7zM2 4.27l2.28 2.28.46.46C3.08 8.3 1.78 10.02 1 12c1.73 4.39 6 7.5 11 7.5 1.55 0 3.03-.3 4.38-.84l.42.42L19.73 22 21 20.73 3.27 3 2 4.27zM7.53 9.8l1.55 1.55c-.05.21-.08.43-.08.65 0 1.66 1.34 3 3 3 .22 0 .44-.03.65-.08l1.55 1.55c-.67.33-1.41.53-2.2.53-2.76 0-5-2.24-5-5 0-.79.2-1.53.53-2.2zm4.31-.78l3.15 3.15.02-.16c0-1.66-1.34-3-3-3l-.17.01z" />
          </svg>
        </div>
      </div>
      <div class="button-group">
        <button type="button" @click="toggleEdit" class="edit-btn">
          {{ isEditing ? 'Cancel' : 'Edit' }}
        </button>
        <button v-if="isEditing" type="submit" class="confirm-btn">
          Confirm
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      password: "",
      newPassword: "",
      confirmPassword: "",
      showPassword: false,
      showPassword2: false,
      showPassword3: false,
      isEditing: false,
      passwordError: "",
      successMessage: "",
    };
  },
  computed: {
    isFormValid() {
      return !this.passwordError;
    },
  },
  methods: {
    validatePassword() {
      if (this.newPassword !== this.confirmPassword) {
        this.passwordError = "The new password and confirmation do not match.";
        this.successMessage = "";
      } else if (this.newPassword.length < 1) {
        this.passwordError = "The password must be at least 1 characters.";
        this.successMessage = "";
      } else {
        this.passwordError = "";
        this.successMessage = "";
      }
    },
    toggleEdit() {
      this.isEditing = !this.isEditing;
      this.oldPassword = "";
      this.newPassword = "";
      this.confirmPassword = "";
      this.passwordError = "";
      this.successMessage = "";
    },
    // Method to handle password edit confirmation
    async confirmEdit() {
      this.validatePassword();
      if (!this.isFormValid) {
        return;
      }

      try {
        const response = await axios.put('http://localhost/api/change_password', {
          old_password: this.password,
          new_password: this.newPassword
        },
          {
            withCredentials: true
          }
        );
        if (response.status === 200) {
          this.successMessage = "Password updated successfully";
          this.passwordError = "";
          this.toggleEdit();
        } else {
          console.error('Error updating password:', response.data);
          alert(response.data.detail || "Failed to update password.");
        }
      } catch (error) {
        console.error('Error updating password:', error);
        alert(error.response?.data?.detail || "An error ocurred whileupdating the password.");
      }
    },
    // Method to toggle password visibility
    togglePassword() {
      this.showPassword = !this.showPassword;
    },
    // Method to toggle new password visibility
    toggleNewPassword() {
      this.showPassword2 = !this.showPassword2;
    },
    // Method to toggle confirm new password visibility
    toggleConfirmPassword() {
      this.showPassword3 = !this.showPassword3;
    },
  },
};
</script>

<style scoped>
.edit-form {
  border: 1px solid #ddd;
  padding: 20px;
  max-width: 750px;
  margin: auto;
  text-align: left;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
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

.input:focus,
.input:hover {
  outline: none;
  border-color: rgba(129, 140, 248);
  background-color: #fff;
  box-shadow: 0 0 0 5px rgb(129 140 248 / 30%);
}

.icon {
  position: absolute;
  left: 1rem;
  fill: none;
  width: 1.5rem;
  height: 1.5rem;
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

.button-group {
  display: flex;
  justify-content: space-between;
}

.edit-btn,
.confirm-btn {
  padding: 15px 25px;
  border: unset;
  border-radius: 15px;
  color: #212121;
  z-index: 1;
  background: #e8e8e8;
  position: relative;
  font-weight: 1000;
  font-size: 17px;
  -webkit-box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  transition: all 250ms;
  overflow: hidden;
}

.edit-btn::before,
.confirm-btn::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 0;
  border-radius: 15px;
  background-color: #212121;
  z-index: -1;
  -webkit-box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  transition: all 250ms
}

.edit-btn:hover,
.confirm-btn:hover {
  color: #e8e8e8;
}

.edit-btn:hover::before,
.confirm-btn:hover::before {
  width: 100%;
}
</style>