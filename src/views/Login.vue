<template>
  <div>
    <h1>This Is The Login</h1>
    <p>Email</p>
    <input type="text" id="email-input" v-model="email" />
    <p>Password</p>
    <input type="password" id="password-input" v-model="password" />
    <br />
    <button @click="loginUser">Login User</button>
    <h3>{{loginStatus}}</h3>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
export default {
  name: "login-page",

  data() {
    return {
      email: "",
      password: "",
      loginStatus:""
    };
  },
  methods: {
    loginUser: function() {
        this.loginStatus = "Loading",
      axios.request({
        url: "https://tweeterest.ml/api/login",
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
        },
        data:{
            email: this.email,
            password: this.password
        }
      }).then((response)=>{
          console.log(response);
           this.loginStatus = "Succesful Login",
          cookies.set("loginToken", response.data.loginToken),
          cookies.set("userId", response.data.userId),
          this.$router.push("/userhp")
      }).catch((error)=> {
          console.log(error)
          this.loginStatus = "Error"
      })
    }
  }
};
</script>

<style lang="scss" scoped>
</style>