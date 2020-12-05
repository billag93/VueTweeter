<template>
  <div>
    <div id="nav-bar_mobile">
      <div>
        <router-link class="nav" to="/discoverpage">
          <img src="@/assets/binoculars.svg" alt="" />
        </router-link>
      </div>
      <div>
        <router-link class="nav" to="/userhp">
          <img src="@/assets/home.svg" alt="" />
        </router-link>
      </div>
      <div>
        <router-link class="nav" to="/userprofile"
          ><img src="@/assets/profile.svg" alt="" />
        </router-link>
      </div>
      <div>
        <router-link class="nav" to="/explorepage">
          <img src="@/assets/internet-explorer.svg" alt="" />
        </router-link>
      </div>
    </div>
    <div id="nav-bar">
      <img src="@/assets/happy-face.svg" alt="Twitter Clone Logo" />
      <div class="nav_link" >
        <img src="@/assets/binoculars.svg" alt="" />
        <router-link  to="/discoverpage">Discover</router-link>
      </div>
      <div class="nav_link">
        <img src="@/assets/home.svg" alt="" />
        <router-link  to="/userhp">User HomePage</router-link>
      </div>
      <div class="nav_link">
        <img src="@/assets/profile.svg" alt="" />
        <router-link  to="/userprofile"
          >User Profile</router-link
        >
      </div>
      <div class="nav_link">
        <img src="@/assets/internet-explorer.svg" alt="" />
        <router-link  to="/explorepage">Explore</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "navigation-bar"
};
</script>

<style lang="scss" scoped>
 
  #nav-bar {
    display: none;
  }

  #nav-bar_mobile {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    width: 100%;
    position: sticky;
    bottom: 0;
    height: 8vh;
    background: deepskyblue;
    border-top: 2px solid dodgerblue;
    img{
      height: 50px;
    }
    .nav{
      display: grid;
      align-items: center;
      justify-items: center;
      border: 3px solid cornflowerblue;
      border-radius: 10%;
      margin: 3% 3%;
      padding: 2% 2%;
      background: cyan;
      
    }
  }
  @media only screen and (min-width: 768px){
    #nav-bar_mobile{
      display: none;
    }
    #nav-bar{
      display: grid;
      text-decoration: none;
    width: 100%;
    position: sticky;
    bottom: 0;
    height: 90vh;
    background: deepskyblue;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    
    img{
      height: 70px;
    }
    .nav_link{
      text-decoration: none;
      display: grid;
      grid-template-columns: 1fr 1fr;
      align-items: center;
      justify-items: center;
      border: 3px solid cornflowerblue;
      border-radius: 10%;
      margin: 3% 3%;
      padding: 2% 2%;
      background: cyan;
      
    }
    }
  }

</style>