<template>
      <h5 class="mb-2">Menu</h5>
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
      >
      <el-menu-item-group title="Modes">
        <el-menu-item index="1" @click="changeMode(1)">
          <el-icon><icon-menu /></el-icon>
          <span>Text</span>
        </el-menu-item>
        <el-menu-item index="2" @click="changeMode(2)">
          <el-icon><icon-menu /></el-icon>
          <span>Speech</span>
        </el-menu-item>
      </el-menu-item-group>
      <el-menu-item-group title="Models">
        <el-menu-item index="3" @click="changeModel(1)">
          <el-icon><document /></el-icon>
          <span>GPT3.5-Turbo</span>
        </el-menu-item>
        <el-menu-item index="4" @click="changeModel(2)">
          <el-icon><document /></el-icon>
          <span>Davinci-003</span>
        </el-menu-item>
      </el-menu-item-group>
      <el-menu-item-group title="Languages">
        <el-menu-item index="5" @click="english()">
          <el-icon><document /></el-icon>
          <span>English</span>
        </el-menu-item>
        <el-menu-item index="6" @click="chinese()">
          <el-icon><document /></el-icon>
          <span>中文</span>
        </el-menu-item>
      </el-menu-item-group>  
      <el-menu-item-group title="Tools">
        <el-menu-item index="7" @click="clear()">
          <el-icon><document /></el-icon>
          <span>Clear</span>
        </el-menu-item>
      </el-menu-item-group>  
      </el-menu>
</template>

<script>
import {onMounted, unmounted, defineComponent, ref, reactive, computed, nextTick, watch} from 'vue';
import {useStore} from 'vuex'
import {getCearHistory,getEnglish,getChinese} from "@/api/api";
import ChatPanel from "@/components/ChatPanel";

export default defineComponent({
  setup(){
    const store = useStore()
    const changeLanguage = (language) => {
      store.commit('changeLanguage', language)
    }
    const changeClear = (clear) => {
      store.commit('changeClear', clear)
    }
    const changeModel = (model) => {
      store.commit('changeModel', model);
      changeClear(1);
    }
    const changeMode = (mode) => {
      store.commit('changeMode', mode);
      changeClear(1);
    }
    function clear() {
        const input={"input":"clear history"}
        const input_json = JSON.stringify(input)
        getCearHistory(input_json)
          .then((res) => console.log(res))
          .catch((err) => console.log(err));
        changeClear(1);
    }

    function chinese() {
        const input={"input":"speak chinese"}
        const input_json = JSON.stringify(input)
        getChinese(input_json)
          .then((res) => console.log(res))
          .catch((err) => console.log(err));
        changeLanguage(2);
        changeClear(1);
    }
    function english() {
        const input={"input":"speak english"}
        const input_json = JSON.stringify(input)
        getEnglish(input_json)
          .then((res) => console.log(res))
          .catch((err) => console.log(err));
        changeLanguage(1);
        changeClear(1);
    }
    return{
      changeModel,changeMode,changeLanguage,
      clear,chinese,english
    }
  },
  components:{
    ChatPanel
  }
})
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
