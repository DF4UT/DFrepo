<template>
  <div>
    <button @click="fetchData">获取数据</button>
    <pre v-if="processedData">{{ processedData }}</pre>
    <p v-else>暂无数据</p>
  </div>
</template>
 
<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
 
const processedData = ref('')
 
const fetchData = async () => {
  try {
    const res = await axios.get('/api/test')
    
    // 方法1：直接处理响应数据（如果数据已经是对象）
    if (typeof res.data === 'object') {
      // 将对象转换为JSON字符串，然后处理反斜杠
      let jsonString = JSON.stringify(res.data, null, 2)
      // 处理双反斜杠：将\\\\替换为\\
      processedData.value = jsonString.replace(/\\\\\\\\/g, '\\\\')
    } else {
      // 方法2：如果数据已经是字符串
      processedData.value = res.data.replace(/\\\\\\\\/g, '\\\\')
    }
    
    console.log('处理后的数据:', JSON.parse(processedData.value))
    
  } catch (error) {
    console.error('获取数据失败:', error)
    processedData.value = '获取数据失败'
  }
}
 
// 可选：组件挂载时自动获取数据
// onMounted(() => {
//   fetchData()
// })
</script>