<!-- TextRenderer.vue -->
<template>
  <div class="text-renderer" v-html="sanitizedHtml"></div>
</template>

<script setup>
import { computed } from 'vue';
import { marked } from 'marked';
import katex from 'katex';
import DOMPurify from 'dompurify';
import 'katex/dist/katex.min.css'; // 引入 Katex 样式

const props = defineProps({
  // 要渲染的数据，可以是任意类型
  data: {
    type: [String, Object, Number, Boolean],
    required: true
  },
  // 手动指定格式：'auto', 'text', 'markdown', 'latex', 'json'
  format: {
    type: String,
    default: 'auto'
  }
});

// 将 LaTeX 公式转换为 HTML（支持行内和块级）
const renderLatex = (text) => {
  // 匹配行内公式 $...$ 和块级公式 $$...$$
  const inlineRegex = /\$([^\$]+?)\$/g;
  const blockRegex = /\$\$([^\$]+?)\$\$/g;

  let html = text;

  // 处理块级公式
  html = html.replace(blockRegex, (match, formula) => {
    try {
      return katex.renderToString(formula, { displayMode: true });
    } catch (e) {
      console.error('LaTeX 渲染错误:', e);
      return match;
    }
  });

  // 处理行内公式
  html = html.replace(inlineRegex, (match, formula) => {
    try {
      return katex.renderToString(formula, { displayMode: false });
    } catch (e) {
      console.error('LaTeX 渲染错误:', e);
      return match;
    }
  });

  return html;
};

// 将 Markdown 转换为 HTML（同时支持内嵌 LaTeX）
const renderMarkdown = (text) => {
  // 先用 marked 解析 Markdown
  let html = marked.parse(text, { async: false });
  // 再解析其中的 LaTeX 公式
  return renderLatex(html);
};

// 自动检测内容格式
const detectFormat = (data) => {
  if (typeof data === 'object') return 'json';
  if (typeof data !== 'string') return 'text';
  const trimmed = data.trim();
  // 简单启发：如果包含 $$ 或 $ 且不是普通文本，则可能是 LaTeX
  if ((trimmed.includes('$$') || trimmed.match(/\$[^\$]+\$/)) && !trimmed.includes('\n')) {
    return 'latex';
  }
  // 如果包含 Markdown 标记，则当作 Markdown
  if (trimmed.match(/^#+\s|^\*|\-|\+|^\d+\.|\[.+\]\(.+\)/m)) {
    return 'markdown';
  }
  return 'text';
};

// 将原始数据转换为 HTML 字符串
const convertToHtml = () => {
  let content = props.data;

  // 根据 format 或自动检测决定处理方式
  let type = props.format;
  if (type === 'auto') {
    type = detectFormat(content);
  }

  switch (type) {
    case 'markdown':
      // 输入应为字符串
      if (typeof content !== 'string') content = String(content);
      return renderMarkdown(content);
    case 'latex':
      // 纯 LaTeX 字符串，直接渲染
      if (typeof content !== 'string') content = String(content);
      return renderLatex(content);
    case 'json':
      // 对象或数组格式化为带缩进的 JSON 字符串（置于 <pre> 中）
      try {
        const jsonStr = JSON.stringify(content, null, 2);
        return `<pre>${escapeHtml(jsonStr)}</pre>`;
      } catch (e) {
        return `<pre>无法序列化的对象</pre>`;
      }
    case 'text':
    default:
      // 纯文本，转义 HTML 特殊字符后显示
      return `<div>${escapeHtml(String(content))}</div>`;
  }
};

// 简单的 HTML 转义（防止 XSS）
const escapeHtml = (str) => {
  return str.replace(/[&<>]/g, (m) => {
    if (m === '&') return '&amp;';
    if (m === '<') return '&lt;';
    if (m === '>') return '&gt;';
    return m;
  });
};

// 最终安全的 HTML
const sanitizedHtml = computed(() => {
  const rawHtml = convertToHtml();
  // 使用 DOMPurify 清洗，允许 katex 生成的特定 class 和 style
  return DOMPurify.sanitize(rawHtml, {
    ADD_TAGS: ['math', 'semantics', 'mrow', 'mi', 'mo', 'mn', 'mtext', 'msup', 'msub', 'msubsup', 'mfrac', 'msqrt', 'mroot', 'mtable', 'mtr', 'mtd'],
    ADD_ATTR: ['target']
  });
});
</script>

<style scoped>
.text-renderer {
  word-break: break-word;
}
.text-renderer pre {
  background: #f5f5f5;
  padding: 10px;
  border-radius: 4px;
  overflow-x: auto;
}
/* Katex 公式默认样式会自带动画等，无需额外处理 */
</style>