import openai
# openai.api_key = ""

message_list=[
    {"role": "system", "content": "You are a helpful assistant."},
]

while(True):
    input_str=input("你:")
    input_message= {"role": "user", "content": input_str}
    message_list.append(input_message)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message_list
    )
    message_list.append(response.choices[0].message)
    print("ChatGPT:"+response.choices[0].message.content)
