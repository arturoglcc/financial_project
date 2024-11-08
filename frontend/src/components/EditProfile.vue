<template>
  <div class="edit-form">
    <h2>Edit profile</h2>
    <form @submit.prevent="confirmEdit">
      <div class="input-group">
        <label for="username">Username</label>
        <div class="input-container group">
          <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" class="icon">
            <path fill="none" stroke="currentColor" d="M18.5 20.247V16S16 14.5 12 14.5S5.5 16 5.5 16v4.247M1.5 12C1.5 6.201 6.201 1.5 12 1.5S22.5 6.201 22.5 12S17.799 22.5 12 22.5S1.5 17.799 1.5 12Zm10.426.5S8.5 10.68 8.5 8c0-1.933 1.569-3.5 3.504-3.5A3.495 3.495 0 0 1 15.5 8c0 2.68-3.426 4.5-3.426 4.5z" />
          </svg>
          <input type="text" id="username" v-model="username" :disabled="!isEditing" class="input" />
        </div>
      </div>
      <div class="input-group">
        <label for="email">Email address</label>
        <div class="input-container group">
          <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 16 16" class="icon">
            <path fill="currentColor" fill-rule="evenodd" d="M14.95 3.684L8.637 8.912a1 1 0 0 1-1.276 0l-6.31-5.228A1 1 0 0 0 1 4v8a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4a1 1 0 0 0-.05-.316M2 2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2m-.21 1l5.576 4.603a1 1 0 0 0 1.27.003L14.268 3z"/>
          </svg>
          <input type="email" id="email" v-model="email" :disabled="!isEditing"  class="input" />
        </div>
      </div>
      <div class="input-group">
        <label for="password">Password</label>
        <div class="input-container group">
          <svg stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="icon">
            <path d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" stroke-linejoin="round" stroke-linecap="round"></path>
          </svg>
          <input :type="showPassword ? 'text' : 'password'" id="password" v-model="password" :disabled="!isEditing" class="input" />
          <svg class="input-icon clickable" viewBox="0 0 24 24" @click="togglePassword">
            <path v-if="showPassword" d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zm0 12c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z" />
            <path v-else d="M12 7c2.76 0 5 2.24 5 5 0 .65-.13 1.26-.36 1.83l2.92 2.92c1.51-1.26 2.7-2.89 3.43-4.75-1.73-4.39-6-7.5-11-7.5-1.4 0-2.74.25-3.98.7l2.16 2.16C10.74 7.13 11.35 7 12 7zM2 4.27l2.28 2.28.46.46C3.08 8.3 1.78 10.02 1 12c1.73 4.39 6 7.5 11 7.5 1.55 0 3.03-.3 4.38-.84l.42.42L19.73 22 21 20.73 3.27 3 2 4.27zM7.53 9.8l1.55 1.55c-.05.21-.08.43-.08.65 0 1.66 1.34 3 3 3 .22 0 .44-.03.65-.08l1.55 1.55c-.67.33-1.41.53-2.2.53-2.76 0-5-2.24-5-5 0-.79.2-1.53.53-2.2zm4.31-.78l3.15 3.15.02-.16c0-1.66-1.34-3-3-3l-.17.01z" />
          </svg>
        </div>
      </div>
      <div class="input-group">
        <label for="fullName">Full name</label>
        <div class="input-container group">
          <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 32 32" class="icon">
            <g fill="currentColor">
              <path d="m15.287 17.527l-.99 3.17a1.005 1.005 0 0 0 .97 1.303h1.466c.688 0 1.173-.662.97-1.304l-.99-3.17c-.213-.701-1.203-.701-1.426 0m-1.87 5.757c.747.39 1.637.612 2.583.612c.956 0 1.836-.222 2.583-.612c.256-.13.53.148.369.39A3.53 3.53 0 0 1 16 25.25a3.53 3.53 0 0 1-2.952-1.577c-.16-.232.114-.52.369-.39M11.542 15.4c-1.214 0-2.24.84-2.527 1.967a.512.512 0 0 0 .503.633h.8a1.664 1.664 0 1 1 3.209 0h.148a.428.428 0 0 0 .424-.504a2.61 2.61 0 0 0-2.557-2.096m8.916 0c1.214 0 2.24.84 2.527 1.967a.512.512 0 0 1-.503.633h-.8a1.664 1.664 0 0 0-1.61-2.108a1.65 1.65 0 0 0-1.658 1.665q0 .236.06.443h-.149a.428.428 0 0 1-.424-.504a2.6 2.6 0 0 1 2.557-2.096" />
              <path d="M11.927 16.611a.947.947 0 0 1 .84 1.389h-1.679a1 1 0 0 1-.108-.443c0-.172.046-.334.127-.473a.295.295 0 0 0 .544-.164a.3.3 0 0 0-.105-.229a.95.95 0 0 1 .381-.08m7.347.421a.94.94 0 0 0-.16.525c0 .157.04.305.11.443h1.678a.947.947 0 0 0-1.182-1.325a.3.3 0 0 1-.17.545a.3.3 0 0 1-.276-.188m2.404-4.649c.575.181.955.483 1.282.767a.517.517 0 0 1-.68.78c-.293-.256-.543-.444-.913-.56c-.378-.12-.927-.176-1.824-.067a.517.517 0 1 1-.126-1.026c.983-.12 1.694-.072 2.26.106m-12.313.747l-.001.002a.517.517 0 0 0 .633.818l.005-.004l.03-.022q.045-.032.14-.09a4.14 4.14 0 0 1 2.585-.53a.517.517 0 1 0 .127-1.027a5.17 5.17 0 0 0-3.242.67a4 4 0 0 0-.253.166l-.016.012l-.006.004z" />
              <path d="M27.415 8.07a4.33 4.33 0 0 0-2.363-1.96c-1.049-.36-1.949-1.05-2.522-2A4.34 4.34 0 0 0 18.822 2c-.604 0-1.177.13-1.701.35c-.712.31-1.513.31-2.225 0a4.5 4.5 0 0 0-1.71-.35c-1.553 0-2.908.82-3.68 2.05a5 5 0 0 1-2.58 2.07c-.164.058-.326.106-.487.155C5.62 6.52 4.836 6.758 4 8.07c-1 1.57-1.12 3.4-.23 4.71c.327.48.505 1.05.505 1.63l.001.67A4 4 0 0 0 3 18.01c0 1.161.494 2.206 1.284 2.937q-.013.519-.034 1.039c0 1.134.925 2.185 1.991 2.933a8.3 8.3 0 0 0 8.008 6.091h3.517a8.3 8.3 0 0 0 8.011-6.104c1.059-.748 1.973-1.792 1.973-2.92l-.002-1.07A4 4 0 0 0 29 18.01a4 4 0 0 0-1.287-2.939v-.661c0-.58.178-1.15.504-1.63c.94-1.35.068-3.18-.802-4.71M7.5 13.3c0-2.926 2.399-5.3 5.29-5.3h2.373a.24.24 0 0 1 .219.151l.007.018l.008.018a5.52 5.52 0 0 0 5.037 3.283h2.587a1.7 1.7 0 0 1 1.593 1.651l-.166 2.768l.887.149a2 2 0 0 1-.216 3.969l-.885.051l-.22 3.504a6.3 6.3 0 0 1-6.248 5.448H14.25A6.3 6.3 0 0 1 8 23.56l-.23-3.504l-.884-.05a2 2 0 0 1-.26-3.961l.254-.048l.62-.091z" />
            </g>
          </svg>
          <input type="text" id="fullName" v-model="fullName" :disabled="!isEditing" class="input" />
        </div>
      </div>
      <div class="input-group">
        <label for="curp">CURP</label>
        <div class="input-container group">
          <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 56 56" class="icon">
            <path fill="currentColor" fill-rule="evenodd" d="M42.853 42.714q-.446-.06-.859-.125c-6.058-.963-6.667-3.117-7.457-4.768c-.642-.277-.957-.5-1.286-1.643c-.142-.488-.388-2.654-.284-3.498c.498-.467.876-1.653 1.04-2.204c.442-1.474.549-1.832.97-3.796c.06-.28.219-.394.348-.442c.392-.142.482-.457.61-.69c.303-.534.043-.774.516-2.077c.604-1.482.698-3.008.24-3.446c-.311-.277-.5-.07-.653-.014c-.102.04-.023-.215.069-.578c.363-1.493.365-2.758.463-4.288c.079-1.239-.004-2.369-.159-3.07c-.146-.145-.523-1.77-.955-2.72c-.738-1.632-2.95-1.885-3.708-2.212c-1.804-.755-4.06-1.778-6.734-.623c-1.19.513-2.775.563-4.5 2.504c-.408.456-1.136.064-1.949 1.84c-.825 1.74-.869 2.886-.681 4.13l-.057.003s.021 2.977.386 4.47c.09.364.167.617.067.579c-.152-.056-.361-.236-.672.042c-.46.438-.216 1.901.388 3.383c.476 1.303.159 1.691.665 2.377c.18.244.348.373.542.455c.13.052.313.068.398.34c.557 2.02.66 2.64 1.239 3.842c.25.519.531 1.818 1.049 2.322c.085.711-.003 2.76-.115 3.371c-.18.961-.517 1.239-1.422 1.643c-.492 1.6-1.797 3.048-7.255 4.722q-.28.086-.571.171q-.156.052-5.545 4.783A2 2 0 0 0 8.301 51h38.907a2 2 0 0 0 1.289-3.53z" />
          </svg>
          <input type="text" id="curp" v-model="curp" :disabled="!isEditing" class="input" />
        </div>
      </div>
      <div class="input-group">
        <label for="rfc">RFC</label>
        <div class="input-container group">
          <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 20 20" class="icon">
            <path fill="currentColor" d="M10.6 9c-.4-.1-.8-.3-1.1-.6c-.3-.1-.4-.4-.4-.6s.1-.5.3-.6c.3-.2.6-.4.9-.3c.6 0 1.1.3 1.4.7l.9-1.2c-.3-.3-.6-.5-.9-.7s-.7-.3-1.1-.3V4H9.4v1.4c-.5.1-1 .4-1.4.8c-.4.5-.7 1.1-.6 1.7c0 .6.2 1.2.6 1.6c.5.5 1.2.8 1.8 1.1c.3.1.7.3 1 .5c.2.2.3.5.3.8q0 .45-.3.9c-.3.3-.7.4-1 .4c-.4 0-.9-.1-1.2-.4c-.3-.2-.6-.5-.8-.8l-1 1.1c.3.4.6.7 1 1c.5.3 1.1.6 1.7.6V16h1.1v-1.5c.6-.1 1.1-.4 1.5-.8c.5-.5.8-1.3.8-2c0-.6-.2-1.3-.7-1.7c-.5-.5-1-.8-1.6-1M10 2c-4.4 0-8 3.6-8 8s3.6 8 8 8s8-3.6 8-8s-3.6-8-8-8m0 14.9c-3.8 0-6.9-3.1-6.9-6.9S6.2 3.1 10 3.1s6.9 3.1 6.9 6.9s-3.1 6.9-6.9 6.9" />
          </svg>
          <input type="text" id="rfc" v-model="rfc" :disabled="!isEditing" class="input" />
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
export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      fullName: "",
      curp: "",
      rfc: "",
      showPassword: false,
      isEditing: false,
    };
  },
  methods: {
    toggleEdit() {
      this.isEditing = !this.isEditing;
    },
    confirmEdit() {
      this.isEditing = false;
    },
    togglePassword() {
      this.showPassword = !this.showPassword;
    },
  },
}
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

.edit-btn, .confirm-btn {
  padding: 15px 25px;
  border: unset;
  border-radius: 15px;
  color: #212121;
  z-index: 1;
  background: #e8e8e8;
  position: relative;
  font-weight: 1000;
  font-size: 17px;
  -webkit-box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
  box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
  transition: all 250ms;
  overflow: hidden;
}

.edit-btn::before, .confirm-btn::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 0;
  border-radius: 15px;
  background-color: #212121;
  z-index: -1;
  -webkit-box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
  box-shadow: 4px 8px 19px -3px rgba(0,0,0,0.27);
  transition: all 250ms
}

.edit-btn:hover, .confirm-btn:hover {
  color: #e8e8e8;
}

.edit-btn:hover::before, .confirm-btn:hover::before {
  width: 100%;
}

</style>