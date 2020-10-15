<template>
  <div>
    <div id="my_tweet" v-for="tweet in tweets" :key="tweet.tweetId">
      <h2 class="tweet_area">{{ tweet.content }}</h2>
      <div v-if="userId==tweet.userId">
      <edit-tweet  :tweetId="tweet.tweetId"></edit-tweet>
      <delete-tweet :tweetId="tweet.tweetId"></delete-tweet>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
import EditTweet from "../components/EditTweet.vue"
import DeleteTweet from "../components/DeleteTweet.vue"
    export default {
        name: "view-tweet",

        components: {
          EditTweet,
          DeleteTweet
        },

        data() {
          return {
            tweets: [],
            userId: cookies.get("userId")
          }
        },

    

        mounted:function() {
          return axios.request({
            url: "https://tweeterest.ml/api/tweets",
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
            },
           data: {
              userId: this.userId,
            }
          })
          .then(response => {
            console.log(response);
           this.tweets = response.data
            
          })
          .catch(error => {
            console.log(error);
          });
        }
        
    }
</script>

<style lang="scss" scoped>
#my_tweet {
  display: grid;
  align-items: center;
  justify-items: center;
  background: deepskyblue;
  border: 2px solid cornflowerblue;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-size: 0.8em;
  .tweet_area {
    border: 5px solid cyan;
    border-radius: 4%;
    margin: 3% 3%;
    padding: 2% 2%;
  }
}
</style>