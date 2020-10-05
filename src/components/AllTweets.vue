<template>
    <div>
        <div v-for="tweet in tweets" :key="tweet.tweetId">
            <h3>{{tweet.username}}</h3>
            <h3>{{tweet.content}}</h3>
            <h3>{{tweet.createdAt}}</h3>
        </div>
    </div>
</template>

<script>

    export default {
        name: "all-tweets",

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