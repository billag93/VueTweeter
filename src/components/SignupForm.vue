<template>
  <div>
    <p>Email</p>
    <input type="text" id="email-input" v-model="email" />
    <p>Username</p>
    <input type="text" id="username-input" v-model="username" />
    <p>Password</p>
    <input type="password" id="password-input" v-model="password" />
    <p>Bio</p>
    <textarea id="" v-model="bio"></textarea>
    <p>Birthday</p>
    <input type="text" id="birthday-input" v-model="birthdate" />
    <br>
    <button @click="signupUser">Sign Up</button>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies"
export default {
  name: "signup-form",
  data() {
    return {
      email: "",
      username: "",
      password: "",
      bio: "",
      birthdate: ""
    };
  },
  methods: {
    signupUser: function() {
      axios.request({
        url: "https://tweeterest.ml/api/users",
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Api-Key" : "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR",
        },
        data: {
          email: this.email,
          password: this.password,
          username: this.username,
          bio: this.bio,
          birthdate: this.birthdate
        }
      }).then((response)=>{
        //   Write logic to ensure token was sent(if statement)
          console.log(response);
          cookies.set("loginToken",response.data[0].loginToken);
      }).catch((error)=>{
          console.log(error)
      })
    }
  }
};
</script>

<style lang="scss" scoped>
</style>