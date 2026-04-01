<!-- // 假设 markdownContent 是你的 '# 标题\n正文内容'
const blob = new Blob([markdownContent], { type: 'text/markdown' });
const link = document.createElement('a');
link.href = URL.createObjectURL(blob);
link.download = 'document.md'; // 文件名
link.click();
URL.revokeObjectURL(link.href); -->

<template>
    <div>
        <textarea v-model="markdownContent" rows="10" cols="50"></textarea>
        <br>
        <button @click="downloadMarkdown">下载Markdown</button>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const markdownContent = ref('')

const blob = new Blob([markdownContent], { type: 'text/markdown' });
const link = document.createElement('a');
link.href = URL.createObjectURL(blob);
link.download = 'document.md'; // 文件名
link.click();
URL.revokeObjectURL(link.href);
</script>
