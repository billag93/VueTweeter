<template>
  <div>
    <div id="login_page">
    <h1 id="user_login">User Login</h1>
    <p>Email</p>
    <input type="text" class="textarea" id="email-input" v-model="email" />
    <p>Password</p>
    <input type="password" class="textarea" id="password-input" v-model="password" />
    <br />
    <button id="loginbutton" @click="loginUser">Login User</button>
    <h3>{{loginStatus}}</h3>
    </div>
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

  #login_page{
  display: grid;
  align-items: center;
  justify-items: center;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  background: deepskyblue;
  color: mintcream;
  #loginbutton{
    margin: 5% 5%;
    padding: 2% 2%; 
    background: dodgerblue;
    color: floralwhite;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    border-radius: 7%;
  }
  .textarea{
      border: 5px solid cyan;
      border-radius: 7%;
      margin: 3% 3%;
      padding: 2% 2%;
    }
}

</style>