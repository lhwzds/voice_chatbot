import openai

# openai.api_key = ""
prompt=""
while(True):
    input_str=input("你:")
    prompt=prompt+"你:"+input_str+"\nChatGPT:"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.5,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["你:"]
    )
    prompt=prompt+response.choices[0].text+"\n"
    print(prompt)

