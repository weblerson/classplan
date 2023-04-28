<template>
<div class="container form-container-size">
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

        <form action="{{ this.action }}" method="POST">
            <!--First Input-->
            <component :is="this.firstInput" />

            <!--Second Input-->
            <component :is="this.secondInput" />
        </form>
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

    props: {
        title: {
            type: String,
            required: true
        },
        action: {
            type: String,
            required: true
        },
        firstInput: {
            type: FormInput,
            required: true
        },
        secondInput: {
            type: FormInput,
            required: true
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

.label-font {
    font-family: 'Carrois Gothic', serif;
    font-style: normal;
    font-weight: 400;
    font-size: 24px;
    line-height: 50px;
    
    color: #000000;
}

.form-container-size {
    width: 48vw;
    height: 47vh;

    box-shadow: 0 4px 20px 10px rgba(0, 0, 0, 0.5);
}
</style>