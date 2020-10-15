<template>
  <div>
    <div id="comment_grid" v-for="comment in comments" :key="comment.commentId">
      <div id="comment_box">
        <h3>{{ comment.content }}</h3>
        <p>{{ comment.createdAt }}</p>
      </div>
      <comment-likes :commentId="comment.commentId"></comment-likes>
      <like-comment :commentId="comment.commentId"></like-comment>
      <unlike-comment :commentId="comment.commentId"></unlike-comment>
      <div v-if="userId == comment.userId">
        <edit-comment :commentId="comment.commentId"></edit-comment>
        <delete-comment :commentId="comment.commentId"></delete-comment>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
import UnlikeComment from "../components/UnlikeComment.vue";
import LikeComment from "../components/LikeComment.vue";
import EditComment from "../components/EditComment.vue";
import DeleteComment from "../components/DeleteComment.vue";
import CommentLikes from "../components/CommentLikes.vue";
export default {
  name: "view-comment",

  data() {
    return {
      comments: [],
      userId: cookies.get("userId")
    };
  },

  components: {
    EditComment,
    DeleteComment,
    CommentLikes,
    LikeComment,
    UnlikeComment
  },

  props: {
    tweetId: {
      type: Number,
      required: true
    }
  },

  mounted: function() {
    axios
      .request({
        url: "https://tweeterest.ml/api/comments",
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
        },
        params: {
          tweetId: this.tweetId
        }
      })
      .then(response => {
        console.log(response);
        this.comments = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  },

 
};
</script>

<style lang="scss" scoped>
#comment_grid {
  display: grid;
  #comment_box {
    display: grid;
    background: deepskyblue;
    border: 2px solid cornflowerblue;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
      Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    font-size: 1.2em;
  }
}
</style>