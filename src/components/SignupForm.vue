<template>
  <div>
    <div id="signup">
    <p>Email</p>
    <input type="text" class="textarea" id="email-input" v-model="email" />
    <p>Username</p>
    <input type="text" class="textarea" id="username-input" v-model="username" />
    <p>Password</p>
    <input type="password" class="textarea" id="password-input" v-model="password" />
    <p>Bio</p>
    <textarea id="bio-input" class="textarea" v-model="bio"></textarea>
    <p>Birthday</p>
    <input type="text" class="textarea" id="birthday-input" v-model="birthdate" />
    <br>
    <button id="signupbutton" @click="signupUser">Sign Up</button>
    
    </div>
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
          cookies.set("userId", response.data[0].userId);
      }).catch((error)=>{
          console.log(error)
      })
    }
  }
};
</script>

<style lang="scss" scoped>

  #signup{
    display: grid;
    .textarea{
      border: 5px solid cyan;
      border-radius: 7%;
      margin: 3% 3%;
      padding: 2% 2%;
    }
    #signupbutton{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
      font-size: 1.5em;
      background: deepskyblue;
      color: floralwhite;
      margin: 2% 2%;
      padding: 3% 3%;
    }
  }

</style>