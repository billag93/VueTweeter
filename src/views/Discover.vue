<template>
  <div>
    <div id="large_view">
      <div>
        <view-other-users id="other_users"></view-other-users>
      </div>
      <navigation-bar></navigation-bar>
    </div>
  </div>
</template>

<script>
import ViewOtherUsers from "../components/ViewOtherUsers.vue";
import NavigationBar from "../components/NavigationBar.vue";
export default {
  name: "discover-page",

  components: {
    NavigationBar,
    ViewOtherUsers
  },

  data: function() {
    return {};
  }
};
</script>

<style lang="scss" scoped>
#other_users {
}
@media only screen and (min-width: 768px){
    #large_view{
        display: grid;
        grid-template-columns:3fr 1fr;
    }
}
</style>