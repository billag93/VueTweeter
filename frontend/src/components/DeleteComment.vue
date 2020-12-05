<template>
    <div>
      <div id="delete_comment">
    <button class="delete_button" @click="deleteComment">Delete Comment</button>
      </div>
    </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
    export default {
        name: "delete-comment",

        props: {
            commentId: {
                type: Number,
                
            },
        },

        methods: {
            deleteComment: function() {
        axios.request({
            url: "https://billastweeter.ml/api/comments",
            method: "DELETE",
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
#delete_comment {
  display: grid;
  align-items: center;
  justify-items: center;
  background: deepskyblue;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 0.8em;
  .delete_button{
    margin: 2% 2%;
    padding: 2% 2%; 
    background: dodgerblue;
    color: floralwhite;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    border-radius: 7%;
     border-radius: 10%;
    box-shadow: 4px 4px 2px darkblue;
  }
}
</style>