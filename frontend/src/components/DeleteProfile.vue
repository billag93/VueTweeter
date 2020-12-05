<template>
  <div>
    <div id="delete_profile">
      <h2>Delete Your Profile</h2>
      <h3>Enter Password</h3>
      <input class="text_area" id="password_input" type="password" v-model="password" />
      <button id="delete_button">Delete</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";

export default {
  name: "delete-profile",

  data() {
    return {
      password: ""
    };
  },

  methods: {
    deleteUser: function() {
      axios
        .request({
          url: "https://billastweeter.ml/api/users",
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
          },
          data: {
            password: this.password,
            loginToken: cookies.get("loginToken")
          }
        })
        .then(response => {
          //   Write logic to ensure token was sent(if statement)
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
#delete_profile{
  display: grid;
  justify-items: center;
  align-items: center;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  background: deepskyblue;
  border: 2px solid cornflowerblue;
  #delete_button{
    margin: 3% 3%;
    padding: 2% 2%; 
    background: dodgerblue;
    color: floralwhite;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    border-radius: 5%;
  }
  .text_area{
    border: 5px solid cyan;
      border-radius: 7%;
      margin: 3% 3%;
      padding: 2% 2%;
  }
}
</style>