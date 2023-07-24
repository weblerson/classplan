<template>
<div class="container bg-transparent">
    <div class="container d-flex justify-content-center">
        <p class="master-font text-light">Plano de Aula</p>
    </div>

    <div class="container rounded-5 bg-light form-container-size">
        <div class="container d-flex align-items-start justify-content-center">
            <p class="title-font mt-1 text-dark">{{ this.title }}</p>
        </div>

        <div class="container">
            <hr class="border border-1 border-black mt-0 mb-0">
        </div>

        <!--Inputs-->
        <FormInput ref="usernameFormInput" v-bind="this.inputProps1" />
        <FormInput ref="emailFormInput" v-bind="this.inputProps2" />

        <div class="mt-3 d-grid col-4 mx-auto">
            <input class="btn btn-dark btn-lg" type="submit" value="Enviar" @click="submitForm">
        </div>
    </div>
</div>
</template>

<script>
import FormInput from "@/components/general/FormInput.vue";

export default {
    name: "AuthForm",

    components: {
        FormInput
    },

  data() {
      return {
        inputProps1: {
          id: "username",
          label: "Nome de Usuário",
          name: "username",
          type: "text"
        },
        inputProps2: {
          id: "email",
          label: "E-mail",
          name: "email",
          type: "email"
        }
      }
  },

    props: {
        title: {
            type: String,
            required: true
        },
    },

  methods: {
    submitForm() {
      const username = this.$refs.usernameFormInput.getValue();
      const email = this.$refs.emailFormInput.getValue();

      // Register request code

      return console.log(`Username: ${username}\nEmail: ${email}`);
    }
  }
}
</script>

<style scoped>
.master-font {
    font-family: 'Carrois Gothic SC', serif;
    font-style: normal;
    font-weight: 400;
    font-size: 58px;
    line-height: 69px;
    text-align: center;

    text-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
}

.title-font {
    font-family: 'Carrois Gothic', serif;
    font-style: normal;
    font-weight: 400;
    font-size: 42px;
    line-height: 57px;
    text-align: center;
}

.form-container-size {
    width: 50vw;
    height: 55vh;

    box-shadow: 0 4px 20px 10px rgba(0, 0, 0, 0.5);
}
</style>