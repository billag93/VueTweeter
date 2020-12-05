<template>
  <div>
    <div id="createTweet">
      <h5>{{tweetStatus}}</h5>
      <input class="text_area" type="textarea" maxlength="200" v-model="tweet" />
      <br />
      <button id="tweetbutton" @click="createTweet">Post Tweet</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
export default {
  name: "create-tweet",

  data() {
    return {
      tweet: "",
      tweetStatus: "Tweet!"
      
    };
  },

  methods: {
    createTweet: function() {
      this.tweetStatus = "Tweeting!"
      axios
        .request({
          url: "https://billastweeter.ml/api/tweets",
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
          },
          data: {
            loginToken: cookies.get("loginToken"),
            content: this.tweet,
          }
        })
        .then(response => {
          this.tweetStatus ="Tweeted!"
          console.log(response);
        })
        .catch(error => {
          this.tweetStatus = "Failed to Tweet!"
          console.log(error);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
#createTweet {
  display: grid;
  align-items: center;
  justify-items: center;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  background: deepskyblue;
  border: 2px solid cornflowerblue;
  .text_area {
    border: 5px solid cyan;
    border-radius: 7%;
    margin: 3% 3%;
    padding: 2% 2%;
    width: 250px;
    height: 80px;
    
  }
  #tweetbutton {
    margin: 5% 5%;
    padding: 2% 2%;
    background: dodgerblue;
    color: floralwhite;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
      Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    border-radius: 7%;
  }
}
</style>