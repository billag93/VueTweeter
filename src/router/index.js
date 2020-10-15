import Vue from "vue";
import VueRouter from "vue-router";
import LandingPage from "../views/LandingPage.vue";
import SignUp from "../views/SignUp.vue";
import LoginPage from "../views/Login.vue";
import UsersHP from "../views/UsersHP.vue";
import DiscoverPage from "../views/Discover.vue";
import UserProfilePage from "../views/UserProfilePage.vue";
import ExplorePage from "../views/Explore.vue"


Vue.use(VueRouter);

const routes = [
  {
    path:"/",
    name: "landing-page",
    component: LandingPage
  },
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
{
  path:"/discoverpage",
  name: "discover-page",
  component: DiscoverPage
},
{
  path:"/userprofile",
  name: "user-profile",
  component: UserProfilePage
},
{
  path:"/explorepage",
  name: "explore-page",
  component: ExplorePage
},
];

const router = new VueRouter({
  routes
});

export default router;
