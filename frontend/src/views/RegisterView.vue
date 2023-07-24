<template>
  <div class="background-image d-flex justify-content-center align-items-center">
      <div class="d-flex align-items-center">
          <RegisterForm :title="this.title" />
      </div>
  </div>
</template>

<script>
import RegisterForm from "@/components/register/RegisterForm.vue";

document.title = 'Cadastre-se';

export default {
    name: "RegisterView",

    data() {
        return {
            title: "Cadastre-se",
        }
    },

    components: {
        RegisterForm,
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