import { createMemoryHistory, createRouter } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/Home.vue'),
    meta: { title: 'Home', showInNav: true }
  },
  {
    path: '/about',
    name: 'about', 
    component: () => import('@/views/About.vue'),
    meta: { title: 'About', showInNav: true }
  },
  {
    path: '/lab',
    name: 'lab',
    component: () => import('@/views/Lab.vue'),
    meta: { title: 'Lab', showInNav: true }
  },
  {
    path: '/page4',
    name: 'page4',
    component: () => import('@/views/Page4.vue'),
    meta: { title: 'Page4', showInNav: true }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/NotFound.vue'),
    meta: { title: '404', showInNav: false }
  }
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router
