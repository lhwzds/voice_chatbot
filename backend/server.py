from copy import deepcopy
from flask import Flask, request, make_response
import json
import openai
import os
import azure.cognitiveservices.speech as speechsdk

# openai.api_key = ""

message_list=[
    {"role": "system", "content": "You are a helpful assistant."},
]
prompt_str=" "

app = Flask(__name__)

@app.route("/speech_recognition", methods=["POST"])
def speech_recognition():
    data = request.get_data()
    data = json.loads(data)
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))

    speech_config.speech_recognition_language="zh-CN"
    
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    msg=speech_recognition_result.text
    return make_response(msg, 200)

@app.route("/speech_synthesis_chinese", methods=["POST"])
def speech_synthesis_chinese():
    data = request.get_data()
    data = json.loads(data)
    input= data["input"]
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='zh-CN-XiaomengNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    speech_synthesis_result = speech_synthesizer.speak_text_async(input).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(input))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
                
    return make_response(input, 200)
       
@app.route("/speech_synthesis_english", methods=["POST"])
def speech_synthesis_english():
    data = request.get_data()
    data = json.loads(data)
    input= data["input"]
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='en-US-JennyNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    speech_synthesis_result = speech_synthesizer.speak_text_async(input).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(input))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
                
    return make_response(input, 200)

@app.route("/response_gpt_text", methods=["POST"])
def response_gpt_text():
    data = request.get_data()
    data = json.loads(data)
    input_message= {"role": "user", "content": data["input"]}
    message_list.append(input_message)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_list
    )
    message_list.append(response.choices[0].message)
    msg=response.choices[0].message.content
    
    return make_response(msg, 200)

@app.route("/response_davinci_text", methods=["POST"])
def response_davinci_text():
    data = request.get_data()
    data = json.loads(data)
    input_message= data["input"]
    global prompt_str
    prompt_str=prompt_str+"你:"+input_message+"\nChatGPT:"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt_str,
    temperature=0.5,
    max_tokens=300,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["你:"]
    )
    prompt_str=prompt_str+response.choices[0].text+"\n"
    msg=response.choices[0].text
    
    return make_response(msg, 200)

@app.route("/getCearHistory", methods=["POST"])
def getCearHistory():
    global message_list
    message_list=[
        {"role": "system", "content": "You are a helpful assistant."},
    ]
    global prompt_str
    prompt_str=" "
    msg="success"
    return make_response(msg, 200)

@app.route("/getChinese", methods=["POST"])
def getChinese():
    global message_list
    message_list=[
        {"role": "system", "content": "请只说中文"},
    ]
    global prompt_str
    prompt_str=" "
    msg="success"
    return make_response(msg, 200)

@app.route("/getEnglish", methods=["POST"])
def getEnglish():
    global message_list
    message_list=[
        {"role": "system", "content": "Please speak english only"},
    ]
    global prompt_str
    prompt_str=" "
    msg="success"
    return make_response(msg, 200)

if __name__ == '__main__':
   app.run(host="127.0.0.1", port=5000)