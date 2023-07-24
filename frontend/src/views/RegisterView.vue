<template>
  <div class="background-image d-flex justify-content-center align-items-center">
      <div class="d-flex align-items-center">
          <AuthForm :title="this.title" />
      </div>
  </div>
</template>

<script>
import AuthForm from "@/components/general/AuthForm.vue";

document.title = 'Cadastre-se';

export default {
    name: "RegisterView",

    data() {
        return {
            title: "Cadastre-se",
        }
    },

    components: {
        AuthForm,
    }
}
</script>

<style scoped>
.background-image {
    background-image: url('../assets/img/registerbackground.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    width: 90vw;
    height: 100vh;
}
</style>