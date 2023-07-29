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
    <FormInput ref="firstNameFormInput" v-bind="this.inputProps3" />
    <FormInput ref="lastNameFormInput" v-bind="this.inputProps4" />

    <div class="mt-3 mb-3 d-grid col-4 mx-auto">
      <input class="btn btn-dark btn-lg" type="submit" value="Enviar" @click="submitForm">
    </div>
  </div>
</div>
</template>

<script>
import FormInput from '@/components/general/FormInput.vue'
const axios = require('axios')

document.title = 'Cadastre-se'

export default {
  name: 'RegisterForm',

  components: {
    FormInput
  },

  data () {
    return {
      inputProps1: {
        id: 'username',
        label: 'Nome de Usuário',
        name: 'username',
        type: 'text',
        errors: []
      },
      inputProps2: {
        id: 'email',
        label: 'E-mail',
        name: 'email',
        type: 'email',
        errors: []
      },
      inputProps3: {
        id: 'first-name',
        label: 'Nome',
        name: 'first-name',
        type: 'text',
        errors: []
      },
      inputProps4: {
        id: 'last-name',
        label: 'Sobrenome',
        name: 'last-name',
        type: 'text',
        errors: []
      },

      backendBaseUrl: ''
    }
  },

  props: {
    title: {
      type: String,
      required: true
    }
  },

  methods: {
    async submitForm () {
      const username = this.$refs.usernameFormInput.getValue()
      const email = this.$refs.emailFormInput.getValue()
      const firstName = this.$refs.firstNameFormInput.getValue()
      const lastName = this.$refs.lastNameFormInput.getValue()

      console.log(username, email, firstName, lastName)

      try {
        const url = `${this.backendBaseUrl}/api/auth/register/`
        const response = await axios.post(url, {
          username: username,
          email: email,
          first_name: firstName,
          last_name: lastName
        })

        console.log(response)
      } catch (err) {
        this.inputProps1.errors = err.response.data.username
        this.inputProps2.errors = err.response.data.email
        this.inputProps3.errors = err.response.data.first_name
        this.inputProps4.errors = err.response.data.last_name
      }
    }
  },

  beforeMount () {
    this.backendBaseUrl = process.env.VUE_APP_BACKEND_BASE_URL
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
  display: flex;
  flex-direction: column;

  width: 50vw;

  margin-bottom: 10px;

  box-shadow: 0 4px 20px 10px rgba(0, 0, 0, 0.5);
}
</style>
