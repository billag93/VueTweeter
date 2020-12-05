<template>
    <div>
        <div class="" id="tweet_card">
            <h3 id="username">{{tweetObject.username}}</h3>
            <p id="content">{{tweetObject.content}}</p>
            <h5 id="created_at">{{tweetObject.createdAt}}</h5>
        </div>
        <div>
            <like-tweet  :tweetId="tweetObject.tweetId"></like-tweet>
            <unlike-tweet  :tweetId="tweetObject.tweetId"></unlike-tweet>
            <br>
            <br>
            <edit-tweet v-if="isOwned" :tweetId="tweetObject.tweetId" ></edit-tweet>
            <delete-tweet v-if="isOwned" :tweetId="tweetObject.tweetId"></delete-tweet>
        </div>
        <div>
            <view-comment :tweetId="tweetObject.tweetId" ></view-comment>
            <create-comment :tweetId="tweetObject.tweetId" ></create-comment>
        </div>
    </div>
</template>

<script>
import cookies from "vue-cookies"
import LikeTweet from "../components/LikeTweet.vue"
import UnlikeTweet from "../components/UnlikeTweet.vue"
import EditTweet from "../components/EditTweet.vue"
import DeleteTweet from "../components/DeleteTweet.vue"
import CreateComment from "../components/CreateComment.vue"
import ViewComment from "../components/ViewComment.vue"
    export default {
        name: "tweet-card",

       components: {
           LikeTweet,
           EditTweet,
           DeleteTweet,
           CreateComment,
           UnlikeTweet,
           ViewComment
       },

        props: {
            tweetObject: {
                type: Object,
                required: true,
            },
        },
        data() {
            return {
                isOwned: cookies.get("userId") == this.tweetObject.userId,
                
            }
        },
    }
</script>

<style lang="scss" scoped>
#tweet_card{
    display: grid;
    background: deepskyblue;
  border: 2px solid cornflowerblue;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    #username{
        display: grid;
        align-items: center;
        justify-items: center;
    }
    #content{
        border: 2px solid darkcyan;
        background: white;
        opacity: 90%;
        border-radius: 10%;
        margin: 2% 2%;
        padding: 3% 3%;
    }
}

</style>