<template>
    <div class="area">
        <button @click="getDT">Get DT</button>
        <p><div v-for="(item, index) in response" :key="index">id:{{ item.id }}<FT :data="item.name" format="latex" />-----</div></p>
    </div>
    <div class="area">
        <p><input v-model="name" type="text" placeholder="请输入文本"></p>
        <p><button @click="post">Post</button></p>
        <p><FT :data=prv format="latex" /></p>
    </div>
</template>

<script setup>
// import api from '@/api'
import axios from 'axios'
import { ref, computed } from 'vue'
import FT from '@/components/AllText.vue'
const response = ref('')
const getDT = async () => {
    const res = await axios.get('/api/test')
    response.value = res.data
    let st = JSON.stringify(res.data, null, 2)
    if(typeof st === 'string'){
        response.value = st.replace(/\\\\/g, '\\')
    }
    else{
        response.value = st
    }
    
    response.value = JSON.parse(response.value)
    console.log(response.value)
}
const name = ref('')
const prv = computed(() => {
    return name.value
})
const post = async () => {
    const res = await axios.post('/api/post', { name: name.value })
    response.value = res.data
    let st = JSON.stringify(res.data, null, 2)    
    console.log(res.data)
}

</script>

<style scoped>
button {
    width: 200px;
    height: 50px;
    padding: 8px 16px;
    border-radius: 5px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.3s ease;
}
.area {
    text-align: center;
    margin: 4px;
    padding: 4px;
    min-width: 400px;
    min-height: 400px;
    border: 1px solid #f00;
}
input {
    width: 200px;
    height: 30px;
    padding: 8px 16px;
    border-radius: 5px;
    font-size: 18px;
}
p div {
    margin: 10px;
}
p {
    margin: 4px;
}
</style>
