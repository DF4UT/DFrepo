<template>
    <ApiTest />
    <AllText :data=data.value format="latex" />
</template>

<script setup>
import ApiTest from '@/components/ApiTest.vue'
import AllText from '@/components/AllText.vue'
import JSONS from '@/components/common/JSONS.vue'

const data = {
    value: '$$\\int_0^\\infty e^{-x^2} dx = \\frac{\\sqrt{\\pi}}{2}$$'
}
</script>
