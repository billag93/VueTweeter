<template>
  <div>
    <div
      id="follower_loop"
      v-for="follower in followers"
      :key="follower.userId"
    >
    </div>
     <div id="my_followers">
        <div>
          <h3>Followers</h3>
        </div>
        <div>
          <h3>{{ followers.length }}</h3>
        </div>
      </div>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
export default {
  name: "followers",

  data: function() {
    return {
      followers: ""
    };
  },

  mounted: function() {
    (this.followers = "Loading"),
      axios
        .request({
          url: "https://billastweeter.ml/api/follows",
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
          this.followers = response.data;
        })
        .catch(error => {
          console.log(error);
          this.followers = "Error";
        });
  }
};
</script>

<style lang="scss" scoped>
#follower_loop {
  display: grid;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 1.2em;
  background: deepskyblue;
  border: 2px solid cornflowerblue;
}
#my_followers {
    display: grid;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 1.2em;
    grid-template-columns: repeat(2, 1fr);
    border: 2px solid cyan;
    border-radius: 5%;
    background: dodgerblue;
  }
</style>