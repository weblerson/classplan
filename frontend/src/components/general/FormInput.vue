<template>
<div class="mt-0">
    <label class="form-label text-black label-font mb-0" :for="this.id">{{ this.label }}:</label>
    <input class="form-control" :id="this.id" :type="this.type" :name="this.name" />
</div>
</template>

<script>
export default {
    name: "FormInput",

    props: {
        id: {
            type: String,
            required: true
        },
        label: {
            type: String,
            required: true
        },
        name: {
            type: String,
            required: true
        },
        type: {
            type: String,
            required: true
        }
    }
}
</script>

<style scoped>
.label-font {
    font-family: 'Carrois Gothic', serif;
    font-style: normal;
    font-weight: 400;
    font-size: 24px;
    line-height: 50px;

    color: #000000;
}
</style>