import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import i18n from './plugins/i18n'
import router from './router'
import VCalendar from 'v-calendar'
import store from './store'

Vue.config.productionTip = false

Vue.use(VCalendar, {
  componentPrefix: 'vc'
})

new Vue({
  vuetify,
  i18n,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
