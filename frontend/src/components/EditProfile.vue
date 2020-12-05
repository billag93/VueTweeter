<template>
  <div>
    <div id="edit_profile">
      <h2>Edit Your Profile</h2>
      <h3>Username</h3>
      <input class="text_area" id="username" type="text" v-model="username" />
      <h3>Bio</h3>
      <textarea class="text_area" id="user_bio" v-model="bio"></textarea>
      <h3>Birthdate</h3>
      <input class="text_area" id="birthdate" type="text" v-model="birthdate" />
      <h3>Change Profile Picture</h3>
      <img id="profile_picture" src="" alt="" />
      <button id="update_button" @click="updateUser">Update Profile</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
export default {
  name: "edit-profile",

  data() {
    return {
      bio: "",
      username: "",
      birthdate: "",
    };
  },

  methods: {
    updateUser: function() {
      axios
        .request({
          url: "https://billastweeter.ml/api/users",
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
          },
          data: {
            bio: this.bio,
            username: this.username,
            birthdate: this.birthdate,
            loginToken: cookies.get("loginToken")
          }
        })
        .then(response => {
          //   Write logic to ensure token was sent(if statement)
          console.log(response);
          this.bio = response.data[0].bio;
          this.username = response.data[0].username;
          this.birthdate = response.data[0].birthdate;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
#edit_profile{
   display: grid;
  justify-items: center;
  align-items: center;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  background: deepskyblue;
  border: 2px solid cornflowerblue;
  .text_area{
     border: 5px solid cyan;
      border-radius: 7%;
      margin: 3% 3%;
      padding: 2% 2%;
  }
  #update_button{
     margin: 3% 3%;
    padding: 2% 2%; 
    background: dodgerblue;
    color: floralwhite;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    border-radius: 5%;
  }

}
</style>