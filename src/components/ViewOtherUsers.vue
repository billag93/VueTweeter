<template>
  <div>
    <div id="user_card" v-for="user in users" :key="user.userId">
      <img
        id="profile_picture"
        src="@/assets/userprofile.svg"
        alt="User profile image"
      />
      <h1>{{ user.username }}</h1>
      <h3 id="user_bio">{{ user.bio }}</h3>
      <h5>{{ user.email }}</h5>
      <h5>{{ user.birthdate }}</h5>
      <div class="follow_button_grid">
        <unfollow v-if="loopThroughFollowed(user.userId)" :userId="user.userId"></unfollow>
        <follow-user v-else :userId="user.userId"></follow-user>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";
import Unfollow from "../components/Unfollow";
import FollowUser from "../components/FollowUser.vue";
export default {
  name: "view-other-users",
  components: {
    Unfollow,
    FollowUser
  },

  data() {
    return {
      followedUsers:[],
    };
  },
  computed: {
    users: function() {
      return this.$store.state.userProfiles;
    }
  },
  mounted: function() {
     this.$store.dispatch("getAllUsers");
     this.getfollowedUsers();

  },
  methods: {
    getfollowedUsers: function() {
      axios.request({
          url: "https://tweeterest.ml/api/follows",
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
          },
          params: {
            userId: cookies.get("userId")
          }
        })
        .then(response => {
          console.log(response);
          this.followedUsers = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    loopThroughFollowed:function(userId){
        for(let index=0; index<this.followedUsers.length; index++){
           if (this.followedUsers[index].userId==userId){
               return true
           }
        }
        return false
    }
  }
};
</script>

<style lang="scss" scoped>
#user_card {
  display: grid;
  align-items: center;
  justify-items: center;
  background: deepskyblue;
  border: 2px solid cornflowerblue;
  border-radius: 5%;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  margin: 2% 2%;
  padding: 2% 2%;
  img {
    height: 80px;
  }
  #user_bio {
    border: 2px solid darkcyan;
    background: white;
    opacity: 90%;
    border-radius: 10%;
    margin: 2% 2%;
    padding: 3% 3%;
  }
  .follow_button_grid {
    display: grid;
    text-align: left;
    background: deepskyblue;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
      Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    font-size: 0.8em;
  }
}
</style>