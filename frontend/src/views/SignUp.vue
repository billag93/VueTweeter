<template>
  <div>
    <div id="sign_up">
    <h1>Sign Up</h1>
    <signup-form></signup-form>
    <router-link id="login" to="/login">Already have an account, Login here!</router-link>
    </div>
  </div>
</template>

<script>
import SignupForm from "../components/SignupForm.vue";
export default {
  name: "signup-page",

  components: {
    SignupForm
  }
};
</script>

<style lang="scss" scoped>

  #sign_up{
  display: grid;
  align-items: center;
  justify-items: center;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  background: deepskyblue;
  color: mintcream;
  #login{
    margin: 5% 5%;
    padding: 2% 2%; 
    background: dodgerblue;
    color: floralwhite;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    border-radius: 7%;

  }
}



</style>