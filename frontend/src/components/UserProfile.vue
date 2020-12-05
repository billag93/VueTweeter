<template>
  <div>
    <div id="userID_card">
      <img
        id="profile_picture"
        src="@/assets/userprofile.svg"
        alt="User profile image"
      />
      <h2 id="username">Welcome Back {{ username }}</h2>
      <div id="current_profile">
        <h2>Email</h2>
        <h3>{{ email }}</h3>
        <h2>Your Bio</h2>
        <h3>{{ bio }}</h3>
        <h2>Birthday</h2>
        <h3>{{ birthdate }}</h3>
      </div>
    </div>
    <followers></followers>
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
      userprofile: "",
      userId: "",
      email: "",
      username: "",
      bio: "",
      birthdate: ""
    };
  },
  mounted: function() {
    (this.userprofile = "Loading"),
      axios
        .request({
          url: "https://billastweeter.ml/api/users",
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
          },
          params: {
            userId: cookies.get("userId")
          }
        })
        .then(response => {
          console.log(response);
          (this.userprofile = "Welcome Back"),
            (this.userId = response.data[0].userId),
            (this.email = response.data[0].email),
            (this.username = response.data[0].username),
            (this.bio = response.data[0].bio),
            (this.birthdate = response.data[0].birthdate);
        })
        .catch(error => {
          console.log(error);
          this.userprofile = "Error";
        });
  }
};
</script>

<style lang="scss" scoped>
#userID_card {
  display: grid;
  justify-items: center;
  align-items: center;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  background: deepskyblue;
  border: 2px solid cornflowerblue;
  img {
    height: 80px;
  }
  #username {
    display: grid;
    align-items: center;
    justify-items: center;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
      Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    font-size: 2em;
  }
  #current_profile{
    background: cyan;
    border: 2px solid cornflowerblue;
    border-radius: 5%;
    margin: 2% 2%;
    padding: 3% 3%;
  }
}
</style>