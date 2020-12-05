<template>
  <div>
    <div id="large_view" class="centerit">
        <div id="other_users">
          <view-other-users ></view-other-users>
        </div>
    </div>
     <navigation-bar class="navigation"></navigation-bar>
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
.centerit{
  display: grid;
  align-items: center;
  justify-items: center;
  #other_users {
  display: grid;
  align-items: center;
  justify-items: center;
  width: 450px;
  height:auto;
  .navigation{
    width: 100%;
  }
}
}

@media only screen and (min-width: 768px){
    #large_view{
        display: grid;
        grid-template-columns:3fr 1fr;
    }
}
</style>