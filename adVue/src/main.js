// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui';
import axios from "axios";
import VueResource from 'vue-resource';
import './assets/theme/index.css';
import './assets/iconfont/iconfont.css';
import echarts from 'echarts'

Vue.config.productionTip = false;
axios.defaults.withCredentials = true; // 让 axios 请求携带 cookie
Vue.prototype.$http = axios;
Vue.prototype.$echarts = echarts


Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
