<template>
    <el-row >
        <el-col :span="24">
            <el-scrollbar height="600px">
                <section class="chatlist">
                    <ul>
                        <div v-for="item in records" :key="item.id">
                            <li class="user" v-if="item.type==1" style="list-style-type:none;">
                                <el-avatar class="avatar" :src="user"/>
                                <div class="time"><cite><i>{{item.time}}</i>User</cite></div>
                                <div class="text" v-html="item.content"></div>
                            </li>
                            <li class="server" v-if="item.type==2" style="list-style-type:none;">
                                    <el-avatar class="avatar"  :src="chatgpt"/>
                                <div class="time"><cite>ChatGPT<i>{{item.time}}</i></cite></div>
                                <div class="text" v-html="item.content"></div>
                            </li>
                        </div>
                    </ul>
                </section>
            </el-scrollbar>
        </el-col>
    </el-row>
    <el-row height="50px">
        <el-col :span="23"  id="input">
            <el-input
            @keyup.enter.native="keyDown"
            v-model="textarea"
            autosize
            type="textarea"
            placeholder="Please input"
            >
            </el-input>
        </el-col>
        <el-col :span="1">
            <el-button @click="send" :icon="Promotion" link type="primary" plain circle />
        </el-col>
    </el-row>
  </template>
  
  <script>
  import {onMounted, unmounted, defineComponent, ref, reactive, computed, nextTick, watch} from 'vue';
  import {Promotion} from '@element-plus/icons-vue'
  import chatgpt from '@/assets/chatgpt.png';
  import user from '@/assets/user.png'
  import {useStore} from 'vuex'
  import {getSpeechRecognition,speech_synthesis_english,speech_synthesis_chinese,getResponseGPTText,getResponseDavinciText} from "@/api/api";


  export default defineComponent({
    setup(){
        const textarea = ref('')
        const date=new Date().toDateString()+" "+new Date().toLocaleTimeString();

        const store = useStore()

        let records=ref([])

        const clear = computed(()=>{
            return store.state.clear;
        })
        watch(clear, (newVal, oldVal) => {
            if(newVal==1){
                records.value=[];
            }
        }, {immediate:true,deep:true});
        const changeClear = (clear) => {
             store.commit('changeClear', clear)
        }

        function send() {
            changeClear(0);
            const modelid=store.state.model;
            const modeid=store.state.mode;
            let newdate=new Date().toDateString()+" "+new Date().toLocaleTimeString();
            if(modeid==1){
                records.value.push({
                    type: 1,
                    time: newdate,
                    content: textarea.value
                });
                const input={"input":textarea.value}
                const input_json = JSON.stringify(input)
                if(modelid==1){
                    getResponseGPTText(input_json)
                    .then((res) => {
                        newdate=new Date().toDateString()+" "+new Date().toLocaleTimeString();
                        records.value.push({
                            type: 2,
                            time: newdate,
                            content: res
                        });
                    })
                    .catch((err) => console.log(err));
                }else{
                    getResponseDavinciText(input_json)
                    .then((res) => {
                        newdate=new Date().toDateString()+" "+new Date().toLocaleTimeString();
                        records.value.push({
                            type: 2,
                            time: newdate,
                            content: res
                        });
                    })
                    .catch((err) => console.log(err));
                }
            }else{
                let input={"input":"speech recognition"}
                let input_json = JSON.stringify(input)
                getSpeechRecognition(input_json)
                .then((res) => {
                    newdate=new Date().toDateString()+" "+new Date().toLocaleTimeString();
                    records.value.push({
                        type: 1,
                        time: newdate,
                        content: res
                    });
                    input={"input":res}
                    input_json = JSON.stringify(input)
                    if(modelid==1){
                        getResponseGPTText(input_json)
                        .then((res) => {
                            newdate=new Date().toDateString()+" "+new Date().toLocaleTimeString();
                            records.value.push({
                                type: 2,
                                time: newdate,
                                content: res
                            });
                            input={"input":res}
                            input_json = JSON.stringify(input) 
                            if(store.state.language==1){
                                speech_synthesis_english(input_json)
                                .then((res) => console.log(res))
                                .catch((err) => console.log(err));
                            }else{
                                speech_synthesis_chinese(input_json)
                                .then((res) => console.log(res))
                                .catch((err) => console.log(err));
                            }
                        })
                        .catch((err) => console.log(err));
                    }else{
                        getResponseDavinciText(input_json)
                        .then((res) => {
                            newdate=new Date().toDateString()+" "+new Date().toLocaleTimeString();
                            records.value.push({
                                type: 2,
                                time: newdate,
                                content: res
                            });
                            input={"input":res}
                            input_json = JSON.stringify(input) 
                            if(store.state.language==1){
                                speech_synthesis_english(input_json)
                                .then((res) => console.log(res))
                                .catch((err) => console.log(err));
                            }else{
                                speech_synthesis_chinese(input_json)
                                .then((res) => console.log(res))
                                .catch((err) => console.log(err));
                            }
                        })
                        .catch((err) => console.log(err));
                    }
                }).catch((err) => console.log(err));

            }
            textarea.value=""
        }

        function keyDown(e) {
            if(e.keyCode==13) { 
                send();
            }  
        }
        return{
            send,keyDown,
            textarea,records,
            chatgpt,user,
            Promotion
        }
    },
    components:{
        
    }
  })
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
    #input{
        box-shadow: var(--el-box-shadow)
    }
    .scrollbar-demo-item {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 50px;
        margin: 10px;
        text-align: center;
        border-radius: 4px;
        background: #ffffff;
        color: var(--el-color-primary);
    }
    .chatlist {
        position: absolute;
        top: 0px;
        bottom: 0px;
        left: 0px;
        right: 0px;
        overflow-y: scroll;
        overflow-x: hidden;
        padding: 10px;
    }
    .chatlist ul {
        min-height: 300px;
    }
    
    .chatlist ul .user {
        text-align: right;
        padding-left: 0;
        padding-right: 60px;
    }
    .chatlist ul .server {
        text-align: left;
        padding-left: 30px;
        padding-right: 0;
    }
    
    .chatlist ul li {
        position: relative;
        /* font-size: 0; */
        margin-bottom: 10px;
        padding-left: 60px;
        min-height: 68px;
    }
 
    .avatar {
        display: inline-block;
        vertical-align: top;
        font-size: 14px;
        position: absolute;
        left: 3px;
    }
    .user .avatar {
        left: auto;
        right: 3px;
    }
    .server .avatar {
        right: auto;
        left: -25px;
    }

    cite {
        left: auto;
        right: 60px;
        text-align: right;
        font-style: normal;
        line-height: 24px;
        font-size: 16px;
        white-space: nowrap;
        color: rgb(13, 12, 12);
        text-align: left;
    }
    
    i {
        font-style: normal;
        padding-left: 5px;
        padding-right: 5px;
        font-size: 12px;
    }
    
    .text {
        position: relative;
        line-height: 22px;
        margin-top: 10px;
        padding: 10px 15px;
        background-color: #eee;
        border-radius: 3px;
        color: #333;
        word-break: break-all;
        max-width: 462px\9;
        display: inline-block;
        vertical-align: top;
        font-size: 14px;
    }
    
    .text:after {
        content: '';
        position: absolute;
        left: -10px;
        top: 15px;
        width: 0;
        height: 0;
        border-style: solid dashed dashed;
        border-color: #eee transparent transparent;
        overflow: hidden;
        border-width: 10px;
    }

    .user .text {
        margin-left: 0;
        text-align: left;
        background-color: #11e15a;
        color: #fff;
    }
    .user .text:after {
        left: auto;
        right: -10px;
        border-top-color: #11e15a;
    }
    .server .text {
        margin-right: 0;
        text-align: right;
        background-color: #444647;
        color: #fff;
    }
    .server .text:after {
        right: auto;
        left: -10px;
        border-top-color: #444647;
    }
  </style>
  