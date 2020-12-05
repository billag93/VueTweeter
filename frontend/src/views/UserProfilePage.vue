<template>
  <div>
    <div id="large_view">
      <div id="user_profile">
        <user-profile></user-profile>
        <edit-profile></edit-profile>
        <delete-profile></delete-profile>
      </div>
      <navigation-bar></navigation-bar>
    </div>
  </div>
</template>

<script>
import NavigationBar from "../components/NavigationBar.vue";
import UserProfile from "../components/UserProfile.vue";
import EditProfile from "../components/EditProfile";
import DeleteProfile from "../components/DeleteProfile.vue";
export default {
  name: "user-profile-page",

  components: {
    NavigationBar,
    UserProfile,
    EditProfile,
    DeleteProfile
  }
};
</script>

<style lang="scss" scoped>
html {
  background: deepskyblue;
}
#user_profile {
  background: deepskyblue;
}
@media only screen and (min-width: 768px) {
  #large_view {
    display: grid;
    grid-template-columns: 3fr 1fr;
  }
}
</style>