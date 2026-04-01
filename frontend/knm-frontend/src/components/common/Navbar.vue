<template>
  <nav class="navbar">
    <ul class="nav-list">
      <li v-for="item in navRoutes" :key="item.path" class="nav-item">
        <router-link 
          :to="item.path" 
          class="nav-link"
          :class="{ 'active': $route.path === item.path }"
        >
          {{ item.meta.title }}
        </router-link>
      </li>
    </ul>
  </nav>
  <router-view></router-view>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'
import { computed } from 'vue'

const router = useRouter()
const route = useRoute()

// 路由筛选，只显示showInNav为true的路由
const navRoutes = computed(() => {
  return router.options.routes.filter(route => 
    route.meta && route.meta.showInNav === true
  )
})
</script>

<style scoped>
.navbar {
  background: rgba(0, 0, 0, 0.2);
  padding: 10px 0;
}

.nav-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: flex;
  gap: 20px;
  justify-content: center;
}

.nav-item {
  margin: 0;
}

.nav-link {
  text-decoration: none;
  color: #fff;
  padding: 8px 16px;
  border-radius: 5px;
  font-size: 18px;
  font-weight: bold;
  transition: all 0.3s ease;
  display: block;
}

.nav-link:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-2px);
}

.nav-link.active {
  background-color: #007bff;
  color: #fff;
  box-shadow: 0 2px 8px rgba(0, 123, 255, 0.3);
}

.nav-link.router-link-exact-active {
  background-color: #0056b3;
}
</style>