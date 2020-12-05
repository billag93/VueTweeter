<template>
    <div>
         <div id="comment_button_grid">
        <button id="like_comment_button" @click="likeComment">Like</button>
         </div>
    </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
    export default {
        name: "like-comment",

        props: {
            commentId: {
                type: Number,
                required: true,
            },
        },

        methods: {
             likeComment: function() {
        axios.request({
            url: "https://billastweeter.ml/api/comment-likes",
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
            },
           data: {
              commentId: this.commentId,
               loginToken: cookies.get("loginToken"),
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
#comment_button_grid{
    display: grid;
    align-items: center;
    grid-template-columns: repeat(2, 1fr);
  justify-items: center;
  text-align: left;
  background: deepskyblue;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 0.8em;
  #like_comment_button{
      margin: 1% 1%;
    padding: 1% 1%; 
    background: dodgerblue;
    color: floralwhite;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    border-radius: 10%;
    box-shadow: 4px 4px 2px darkblue;
  }
}
</style>