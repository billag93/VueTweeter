<template>
    <div>
        <div v-for="user in users" :key="user.userId">
            <h3>{{user.bio}}</h3>
            <h3>{{user.username}}</h3>
            <unfollow :userId="user.userId"></unfollow>
            <follow-user :userId="user.userId"></follow-user>
        </div>
    </div>
</template>

<script>
import Unfollow from "../components/Unfollow"
import FollowUser from "../components/FollowUser.vue"
    export default {
        name: "view-other-users",
        components: {
            Unfollow,
            FollowUser
        },
        computed: {
            users:function() {
                return this.$store.state.userProfiles 
            }
        },
        mounted: function() {
           return this.$store.dispatch("getAllUsers")
        
        },
    }
</script>

<style lang="scss" scoped>

</style>