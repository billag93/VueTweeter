<template>
    <div>
        <user-profile></user-profile>
        <edit-profile></edit-profile>
        <delete-profile></delete-profile>
        <view-other-users></view-other-users>
    </div>
</template>

<script>
import UserProfile from "../components/UserProfile.vue"
import EditProfile from "../components/EditProfile.vue"
import DeleteProfile from "../components/DeleteProfile.vue"
import ViewOtherUsers from "../components/ViewOtherUsers.vue"
    export default {
        name: "users-homepage",
        components: {
            UserProfile,
            EditProfile,
            DeleteProfile,
            ViewOtherUsers
        },
    }

</script>

<style scoped>

</style>