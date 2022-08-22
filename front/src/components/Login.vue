<template>
    <div>
        <input v-model="login" type="text" placeholder="Login"/>
        <input v-model="password" type="password" placeholder="Password"/>
        <button @click="checkLoginInfo">Login</button>
    </div>

</template>

<script>
import $ from 'jquery'
export default {
    name: "Login",
    data(){
        return {
            login: '',
            password: '',
        }
    },
    methods: {
        checkLoginInfo() {
            $.ajax({
                url: this.drfURI + "auth/login/",
                type: "POST",
                data: {
                    username: this.login,
                    password: this.password
                },
                success: (response) => {                    
                    sessionStorage.setItem('token', response.token)
                    this.$router.push({name: "shipments"})
                },
                error: (response) => {
                    if (response.status >= 400) {
                        alert("invalid credentials")
                    }
                }
            })
        }
    }
}
</script>

<style scoped>

</style>