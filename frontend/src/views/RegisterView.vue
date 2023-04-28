<template>
  <div class="background-image d-flex justify-content-center align-items-center">
      <div class="d-flex align-items-center">
          <AuthForm :title="this.title">
            <FormInput :is="this.firstInput" v-bind="this.props1"/>
            <FormInput :is="this.secondInput" v-bind="this.props2" />
          </AuthForm>
      </div>
  </div>
</template>

<script>
import AuthForm from "@/components/general/AuthForm.vue";
import FormInput from "@/components/general/FormInput.vue";

document.title = 'Cadastre-se';

export default {
    name: "RegisterView",

    data() {
        return {
            title: "Cadastre-se",
            firstInput: FormInput,
            secondInput: FormInput,
            props1: {
                id: "username",
                label: "Nome de Usuário",
                name: "username",
                type: "text"
            },
            props2: {
                id: "email",
                label: "E-mail",
                name: "email",
                type: "email"
            }
        }
    },

    components: {
        AuthForm,
        FormInput
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