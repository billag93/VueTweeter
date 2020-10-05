<template>
    <div>
        <h2>Delete Your Profile</h2>
        <h3>Enter Password</h3>
        <input id="password_input" type="password" v-model="password">
        <button>Delete</button>
    </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies"

    export default {
        name: "delete-profile",

        data() {
            return {
               password: "",
            }
        },

        methods: {
           deleteUser: function() {
      axios.request({
        url: "https://tweeterest.ml/api/users",
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "X-Api-Key" : "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR",
        },
        data: {
          password: this.password,
          loginToken: cookies.get("loginToken")
        }
      }).then((response)=>{
        //   Write logic to ensure token was sent(if statement)
          console.log(response);
      }).catch((error)=>{
          console.log(error)
      })
    }
        },
    }
</script>

<style lang="scss" scoped>

</style>