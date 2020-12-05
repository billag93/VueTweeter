<template>
  <div>
    <div id="large_view">
      <div>
        <user-profile></user-profile>
        <create-tweet></create-tweet>
        <view-tweet></view-tweet>
      </div>
      <div>
        <navigation-bar></navigation-bar>
      </div>
    </div>
  </div>
</template>

<script>
import UserProfile from "../components/UserProfile.vue";
import CreateTweet from "../components/CreateTweet.vue";
import NavigationBar from "../components/NavigationBar.vue";
import ViewTweet from "../components/ViewTweet.vue";
export default {
  name: "users-homepage",
  components: {
    UserProfile,
    NavigationBar,
    CreateTweet,
    ViewTweet
  }
};
</script>

<style lang="scss" scoped>
@media only screen and (min-width: 768px){
    #large_view{
        display: grid;
        grid-template-columns:3fr 1fr;
    }
}
</style>