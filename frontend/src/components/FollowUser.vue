<template>
  <div>
      <div>
      <button id="follow_user" @click="followUser">follow</button>
      </div>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
export default {
  name: "follow-user",

  data() {
    return {
      
    }
  },

  props: {
    userId: {
      type: Number,
    },
  },

  methods: {
    followUser: function () {
      axios
        .request({
          url: "https://billastweeter.ml/api/follows",
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR",
          },
          data: {
            loginToken: cookies.get("loginToken"),
            followId: this.userId,
          },
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
#follow_user {
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