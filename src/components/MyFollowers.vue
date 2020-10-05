<template>
    <div>
        <h3>Followers {{followers}}</h3>
    </div>
</template>

<script>
import axios from "axios"
import cookies from "vue-cookies"
    export default {
        name: "followers",

        data: function() {
            return {
                followers:"",
            }
        },

        mounted:function() {
            this.followers= "Loading",
      axios.request({
        url: "https://tweeterest.ml/api/follows",
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
        },
            params:{
            userId: cookies.get("userId")
        }
      }).then((response)=>{
          console.log(response);
           this.followers = response.data[0,1,2]
         
      }).catch((error)=> {
          console.log(error)
          this.followers = "Error"
      })
        },


    }
</script>

<style lang="scss" scoped>

</style>