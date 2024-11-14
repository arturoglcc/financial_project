import { createRouter, createWebHistory } from "vue-router";
import Login from "./components/Login.vue";
import SignUp from "./components/SignUp.vue";
import Home from "./views/Home.vue";
import UserSettings from "./views/UserSettings.vue";
import ChangePassword from "./views/ChangePassword.vue";
import AddIncome from "./views/AddIncome.vue";
import AddOutlay from "./views/AddOutlay.vue";

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login,
  },
  {
    path: "/signup",
    name: "SignUp",
    component: SignUp,
  },
  {
    path: "/home",
    name: "Home",
    component: Home,
  },
  {
    path: "/user-settings",
    name: "User settings",
    component: UserSettings,
  },
  {
    path: "/change-password",
    name: "Change Password",
    component: ChangePassword,
  },
  {
    path: "/add-income",
    name: "Add Income",
    component: AddIncome,
  },
  {
    path: "/add-outlay",
    name: "Add Outlay",
    component: AddOutlay,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
