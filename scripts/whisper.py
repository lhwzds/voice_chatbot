# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
# openai.api_key = ""
audio_file= open("audio/CASS-C_123.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
message_list=[
    {"role": "system", "content": "You are a helpful assistant."},
]
input_message= {"role": "user", "content": transcript.text}
message_list.append(input_message)
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_list
)
message_list.append(response.choices[0].message)
print("ChatGPT:"+response.choices[0].message.content)
