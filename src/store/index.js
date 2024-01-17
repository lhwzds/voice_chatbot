import {createStore} from 'vuex'

export default createStore({
    state: {
        mode:1,
        language:1,
        model:1,
        clear:1,
    },

    mutations: {
        changeMode(state, id) {
            state.mode = id
        },
        changeLanguage(state,id){
            state.language = id
        },
        changeModel(state,id){
            state.model=id
        },
        changeClear(state,id){
            state.clear=id
        }
    },

    actions: {}

})
    
