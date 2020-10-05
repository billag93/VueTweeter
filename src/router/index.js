import Vue from "vue";
import VueRouter from "vue-router";
import SignUp from "../views/SignUp.vue";
import LoginPage from "../views/Login.vue";
import UsersHP from "../views/UsersHP.vue";


Vue.use(VueRouter);

const routes = [
 {
   path:"/signup",
   name: "signup-page",
   component: SignUp
 },
 {
  path:"/login",
  name: "login-page",
  component: LoginPage
},
{
  path:"/userhp",
  name: "user-homepage",
  component: UsersHP 
},
];

const router = new VueRouter({
  routes
});

export default router;
