<template>
    <div>
      <div id="comment_likes">
        <h3>Comment Likes</h3>
        <h3>{{commentLikes.length}}</h3>
      </div>
    </div>
</template>

<script>
import axios from "axios"
    export default {
        name: "comment-likes",

        data: function() {
          return {
            commentLikes: "",
          }
        },

        props: {
            commentId: {
                type: Number,
               
            },
        },

        mounted: function() {
          (this.commentLikes = "Loading!") 
        axios.request({
            url: "https://tweeterest.ml/api/comment-likes",
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
            },
           data: {
              commentId: this.commentId,
            
            }
          })
          .then(response => {
            console.log(response);
            this.commentLikes == response.data
          })
          .catch(error => {
            console.log(error);
          });
    
        },
    }
</script>

<style lang="scss" scoped>


</style>