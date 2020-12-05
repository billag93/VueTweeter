<template>
  <div>
    <button id="unfollow_user" @click="unfollowUser">Unfollow</button>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
export default {
  name: "unfollow",

  props: {
    userId: {
      type: Number
    }
  },

  data: function() {
    return {
      unfollow: ""
    };
  },

  methods: {
    unfollowUser() {
      (this.unfollow = "Loading"),
        axios
          .request({
            url: "https://billastweeter.ml/api/follows",
            method: "DELETE",
            headers: {
              "Content-Type": "application/json",
              "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
            },
            data: {
              followId: this.userId,
              loginToken: cookies.get("loginToken")
            }
          })
          .then(response => {
            console.log(response);
          })
          .catch(error => {
            console.log(error);
            this.unfollow = "Error";
          });
    }
  }
};
</script>

<style lang="scss" scoped>
#unfollow_user {
  margin: 1% 1%;
  padding: 1% 1%;
  background: dodgerblue;
  color: floralwhite;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  border-radius: 10%;
  box-shadow: 4px 4px 2px darkblue;
}
</style>