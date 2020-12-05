import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userProfiles:[],
    usersTweets:[]
  },
  mutations: {
    allUsers: function(state, userinformation){
      state.userProfiles = userinformation;
    },
    allTweets: function(state, userTweets){
      state.usersTweets = userTweets;
    }
  },
  actions: {
    getAllUsers: function(context){
      axios.request({
        url: "https://billastweeter.ml/api/users",
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
        },
      }).then((response)=>{
        console.log(response)
        context.commit('allUsers', response.data);
      }).catch((error)=>{
        console.log(error)
      });
    },
    getAllTweets: function(context){
      axios.request({
        url: "https://billastweeter.ml/api/tweets",
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "X-Api-Key": "iTBBjd87QMFVybPhoCVB3FN6YlhwE6k39MTSSSC9CENwR"
        },
      }).then((response)=>{
        console.log(response)
        context.commit('allTweets', response.data);
      }).catch((error)=>{
        console.log(error)
      });
    }
  },
  modules: {}
});
