<template>
    <el-container :style="{height:state.hHeight+'px'}">
      <el-aside width="20%" >
        <SidePanel></SidePanel>
      </el-aside>
      <el-main width="80%" >
        <ChatPanel></ChatPanel>
      </el-main>
    </el-container>
</template>

<script>
import {onMounted, unmounted, defineComponent, ref, reactive, computed, nextTick, watch} from 'vue';
import ChatPanel from "@/components/ChatPanel";
import SidePanel from "@/components/SidePanel";


export default defineComponent({
  setup(){
    const state = reactive({
      hHeight: document.documentElement.clientHeight - 100,
    })

    return{
      state
    }
  },
  components:{
    ChatPanel,SidePanel
  }
})
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
