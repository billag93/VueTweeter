<template>
  <div>
    <div id="large_view">
      <div id="explore_grid" v-for="tweet in tweets" :key="tweet.tweetId">
        <tweet-card :tweetObject="tweet"></tweet-card>
      </div>
      <div>
        <navigation-bar></navigation-bar>
      </div>
    </div>
  </div>
</template>

<script>
import TweetCard from "../components/TweetCard.vue";
import NavigationBar from "../components/NavigationBar.vue";
export default {
  name: "explore-page",

  components: {
    NavigationBar,
    TweetCard
  },
  computed: {
    tweets: function() {
      return this.$store.state.usersTweets;
    }
  },

  mounted: function() {
    return this.$store.dispatch("getAllTweets");
  }
};
</script>

<style lang="scss" scoped>
html {
  background: deepskyblue;
}
@media only screen and (min-width: 768px) {
  #large_view {
    display: grid;
    grid-template-columns: 3fr 1fr;
    #explore_grid{
      
    }
  }
}
</style>