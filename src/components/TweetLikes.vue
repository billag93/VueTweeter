<template>
    <div>

    </div>
</template>

<script>
import axios from "axios";
    export default {
        name:"tweet-likes",

        props: {
            tweetId: {
                type: Number,
                
            },
        },
        
       mounted: {
        tweetLikes: function() {
        axios.request({
            url: "https://tweeterest.ml/api/comments",
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
            },
           data: {
              tweetId: this.tweetId,
            }
          })
          .then(response => {
            console.log(response);
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