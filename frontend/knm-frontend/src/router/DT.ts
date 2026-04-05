import { createMemoryHistory, createRouter } from 'vue-router'

const routes = [{ path: '/:pathMatch(.*)*', component: () => import('../views/NotFound.vue') }]

const router = createRouter({
    history: createMemoryHistory(),
    routes,
})

export default router
