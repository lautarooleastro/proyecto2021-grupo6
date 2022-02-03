import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import InfoMap from '../views/InfoMap.vue'
import Denuncia from '../views/Issue.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/mapa-informativo',
    name: 'Mapa informativo',
    component: InfoMap
  },
  {
    path: '/denunciar',
    name: 'Denuncia',
    component: Denuncia
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
