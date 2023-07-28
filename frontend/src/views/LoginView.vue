<template>
  <div class="background-image d-flex justify-content-center align-items-center">
    <div class="d-flex align-items-center">
      <LoginForm :title="this.title"/>
    </div>
  </div>
</template>

<script>
import LoginForm from '@/components/login/LoginForm.vue'

document.title = 'Entre'

export default {
  name: 'LoginView',

  data () {
    return {
      title: 'Entre'
    }
  },

  components: {
    LoginForm
  }
}
</script>

<style scoped>
.background-image {
  background-image: url('../assets/img/loginbackground.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;

  width: 90vw;
  height: 100vh;
}
</style>
