<template>
  <div>
    <input type="textarea" maxlength="200" v-bind="tweet" />
    <button @click="createTweet">Tweet</button>
  </div>
</template>

<script>
    export default {
        name: "create-tweet",

        data() {
            return {
               tweet:"",
            }
        },

        methods: {
        createTweet: function() {
        (this.content = "Loading"),
        axios.request({
            url: "https://tweeterest.ml/api/follows",
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
            },
           data: {
              loginToken: cookies.get("loginToken"),
              content= this.tweet
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