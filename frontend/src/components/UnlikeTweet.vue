<template>
  <div>
    <div id="unlike_button_grid">
      <button id="unlike_button" @click="unlikeTweet">Unlike</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
export default {
  name: "unlike-tweet",

  props: {
    tweetId: {
      type: Number
    }
  },

  methods: {
    unlikeTweet: function() {
      axios
        .request({
          url: "https://billastweeter.ml/api/tweet-likes",
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
          },
          data: {
            tweetId: this.tweetId,
            loginToken: cookies.get("loginToken")
          }
        })
        .then(response => {
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
#unlike_button_grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  align-items: center;
  justify-items: center;
  background: deepskyblue;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 0.8em;
  #unlike_button {
    margin: 1% 1%;
    padding: 1% 1%;
    background: dodgerblue;
    color: floralwhite;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
      Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    border-radius: 10%;
    box-shadow: 4px 4px 2px darkblue;
    #unlike_button:hover {
      cursor: pointer;
    }
  }
}
</style>