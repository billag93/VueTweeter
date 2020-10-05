<template>
    <div>
        <div id="userID_card">
        <h2>Welcome Back {{username}}</h2>
        <h3>{{email}}</h3>
        <h3>{{bio}}</h3>
        <h3>{{birthday}}</h3>
        <followers></followers>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
import Followers from "../components/MyFollowers.vue";
export default {
  name: "user-profile",

  components: {
    Followers
  },

  data() {
    return {
      userprofile:"",
      userId: "",
      email: "",
      username:"",
      bio:"",
      birthday:""
    };
  },
     mounted: function() {
        this.userprofile = "Loading",
      axios.request({
        url: "https://tweeterest.ml/api/users",
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
        },
            params:{
            userId: cookies.get("userId")
        }
      }).then((response)=>{
          console.log(response);
           this.userprofile= "Welcome Back",
            this.userId= response.data[0].userId,
            this.email= response.data[0].email,
            this.username= response.data[0].username,
            this.bio= response.data[0].bio,
            this.birthday= response.data[0].birthday
         
      }).catch((error)=> {
          console.log(error)
          this.userprofile = "Error"
      })
    }
};
</script>

<style scoped>

</style>