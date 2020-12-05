<template>
    <div>
      <h2>{{totalTweetlikes.length}}</h2>
    </div>
</template>

<script>
import axios from "axios";
    export default {
        name:"tweet-likes",

        data() {
          return {
           totalTweetlikes:[]
          }
        },

        props: {
            tweetId: {
                type: Number,
                
            },
        },
        
       mounted: {
        tweetLikes: function() {
        axios.request({
            url: "https://billastweeter.ml/api/tweet-likes",
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
            },
           params: {
              tweetId: this.tweetId,
            }
          })
          .then(response => {
            console.log(response);
            this.totalTweetlikes==response.data;
          })
          .catch(error => {
            console.log(error);
          });
    }
       },

    }
</script>

<style lang="scss" scoped>

</style>