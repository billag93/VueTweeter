<template>
    <div> 
      <div id="create_comment">
     <input class="text_area" type="textarea" maxlength="150" v-model="content" />
      <button id="comment_button" @click="createComment">Comment</button>
      </div>
    </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
    export default {
        name: "create-comment",

        data: function() {
            return {
                content: "",
            }
        },

        props: {
            tweetId: {
                type: Number,
            },
        },

        methods: {
              createComment: function() {
        axios.request({
            url: "https://billastweeter.ml/api/comments",
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
            },
           data: {
              tweetId: this.tweetId,
              content: this.content,
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
#create_comment{
   display: grid;
  align-items: center;
  justify-items: center;
  background: deepskyblue;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 0.8em;
  .text_area{
    border: 5px solid cyan;
    border-radius: 4%;
    margin: 3% 3%;
    padding: 2% 2%;
  }
  #comment_button{
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