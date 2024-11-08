import { createRouter, createWebHistory } from "vue-router";
import Login from "./components/Login.vue";
import SignUp from "./components/SignUp.vue";
import Home from "./views/Home.vue";
import UserSettings from "./views/UserSettings.vue";

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
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
