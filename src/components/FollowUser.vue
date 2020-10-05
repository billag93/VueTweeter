<template>
  <div>
    <button @click="followUser">follow</button>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
export default {
  name: "follow-user",

  props: {
      userId: {
          type: Number,
      },
  },


  methods: {
    followUser: function() {
        axios.request({
            url: "https://tweeterest.ml/api/follows",
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
            },
           data: {
              loginToken: cookies.get("loginToken"),
              followId: this.userId
            }
          })
          .then(response => {
            console.log(response);
          })
          .catch(error => {
            console.log(error)
          });
    }
  }
};
</script>

<style lang="scss" scoped>
</style>