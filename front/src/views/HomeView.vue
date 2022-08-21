<template>
  <div class="home">
    <img alt="Cargo logo" src="../assets/logo.png">
    <Hello msg="Welcome to Cargo App"/>
    <button @click="toLogin">Login</button>
  </div>
</template>

<script>
// @ is an alias to /src
import Hello from '@/components/Hello.vue'

export default {
  name: 'HomeView',
  components: {
    Hello
  },
  methods: {
    toLogin() {
      this.$router.push({name: 'login'})
    }
  }
}
</script>
