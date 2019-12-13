import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
const router = new Router({
  routes: [
      {
      path: '/',
      name: 'upload',
      component: () => import('../components/Upload'),
      meta: {
        title: "评分上传",
        navIndex: '/upload'
      }
    },
    {
      path: '/bar3d',
      name: 'bar3d',
      component: () => import('../components/Bar3d'),
      meta: {
        title: "3d柱状图",
        navIndex: '/'
      }
    },
    {
      path: '/upload',
      name: 'upload',
      component: () => import('../components/Upload'),
      meta: {
        title: "上传",
        navIndex: '/upload'
      }
    }
  ]
})

export default router;