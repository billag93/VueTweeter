<template>
  <div>
    <div id="landing_page">
      <h1 id="title">Welcome to Twatter!</h1>
      <img src="@/assets/happy-face.svg" alt="logo" />
      <router-link class="login_buttons" to="/login">Login here</router-link>
      <router-link class="login_buttons" to="/signup">Sign Up</router-link>
    </div>
  </div>
</template>

<script>
export default {

};
</script>

<style lang="scss" scoped>
#landing_page{
  display: grid;
  align-items: center;
  justify-items: center;
   background:white;
  border: 10px solid cornflowerblue;
  border-radius: 10%;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  margin: 2% 2%;
  padding: 2% 2%;
  height: 90vh;
  #title{
    display: grid;
    align-items: center;
    justify-items: center;
    text-align: center;
    background:skyblue;
    color: snow;
    text-shadow:2px 2px darkblue;
  border: 10px solid cornflowerblue;
  border-radius: 15%;
  box-shadow: 4px 4px 2px darkblue;
  }
  img{
    height: 200px;
  }
  .login_buttons{
    text-decoration: none;
     margin: 5% 5%;
    padding: 5% 5%; 
    background: dodgerblue;
    color: floralwhite;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    border-radius: 7%;
     box-shadow: 4px 4px 2px darkblue;
  }
}
</style>