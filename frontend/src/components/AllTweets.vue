<template>
    <div>
        <div v-for="tweet in tweets" :key="tweet.tweetId">
            <tweet-card :tweetObject="tweet" ></tweet-card>
            <delete-tweet :tweetId="tweet.tweetId"></delete-tweet>
            <edit-tweet :tweetId="tweet.tweetId"></edit-tweet>
            <view-comment :tweetId="tweet.tweetId"></view-comment>
            <create-comment :tweetId="tweet.tweetId"></create-comment>
            <tweet-likes :tweetId="tweet.tweetId"></tweet-likes>
            <like-tweet :tweetId="tweet.tweetId"></like-tweet>
            <unlike-tweet :tweetId="tweet.tweetId"></unlike-tweet>
        </div>
        
    </div>
</template>

<script>
import TweetCard from "../components/TweetCard.vue"
import DeleteTweet from "../components/DeleteTweet.vue";
import EditTweet from "../components/EditTweet.vue";
import ViewComment from "../components/ViewComment.vue";
import CreateComment from "../components/CreateComment.vue";
import TweetLikes from "../components/TweetLikes.vue";
import LikeTweet from "../components/LikeTweet.vue";
import UnlikeTweet from "../components/UnlikeTweet";
    export default {
        name: "all-tweets",

        components: {
            TweetCard,
            DeleteTweet,
            EditTweet,
            ViewComment,
            CreateComment,
            TweetLikes,
            LikeTweet,
            UnlikeTweet,
        },

        computed: {
            tweets: function() {
                return this.$store.state.usersTweets
            }
        },

      mounted:function(){
         return this.$store.dispatch("getAllTweets")
      },

    }
</script>

<style lang="scss" scoped>

</style>