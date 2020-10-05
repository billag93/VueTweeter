<template>
    <div>
        <h3>Bio</h3>
    <textarea id="user_bio" v-model="bio"></textarea>
        <h3>Change Profile Picture</h3>
        <img id="profile_picture" src="" alt="">
        <button @click="updateUser">Update Profile</button>
    </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies"
    export default {
        name: "edit-profile",

        data() {
            return {
                bio: "",

            }
        },

        methods: {
            updateUser: function() {
      axios.request({
        url: "https://tweeterest.ml/api/users",
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          "X-Api-Key" : "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR",
        },
        data: {
          bio: this.bio,
          loginToken: cookies.get("loginToken")
        }
      }).then((response)=>{
        //   Write logic to ensure token was sent(if statement)
          console.log(response);
         this.bio = response.data[0].bio;
      }).catch((error)=>{
          console.log(error)
      })
    }
        },
    }
</script>

<style lang="scss" scoped>

</style>