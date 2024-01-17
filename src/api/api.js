import { param } from 'jquery'
import http from './http.js'

export function getSpeechRecognition(params) {
    return http.post("local/speech_recognition",params)
}  

export function speech_synthesis_english(params) {
    return http.post("local/speech_synthesis_english",params)
}  

export function speech_synthesis_chinese(params) {
    return http.post("local/speech_synthesis_chinese",params)
}  

export function getResponseGPTText(params) {
    return http.post("local/response_gpt_text",params)
}  

export function getResponseDavinciText(params) {
    return http.post("local/response_davinci_text",params)
}  

export function getCearHistory(params) {
    return http.post("local/getCearHistory",params)
}  

export function getEnglish(params) {
    return http.post("local/getEnglish",params)
}  

export function getChinese(params) {
    return http.post("local/getChinese",params)
}  