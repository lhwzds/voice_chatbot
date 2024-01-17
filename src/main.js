import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import createStore from './store/index.js'
import 'element-plus/dist/index.css'
const app = createApp(App)
app.use(createStore)
app.use(ElementPlus);
app.mount('#app')