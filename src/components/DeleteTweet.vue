<template>
    <div>
        <button @click="deleteTweet">Delete Tweet</button>
    </div>
</template>

<script>
    export default {
        name: "delete-tweet",

        props: {
            tweetId: {
                type: Number,
            },
        },

        methods: {
        deleteTweet: function() {
      (this.content = "Loading"),
        axios.request({
            url: "https://tweeterest.ml/api/tweets",
            method: "DELETE",
            headers: {
              "Content-Type": "application/json",
              "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
            },
           data: {
              loginToken: cookies.get("loginToken"),
              tweetId= this.tweetId 
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