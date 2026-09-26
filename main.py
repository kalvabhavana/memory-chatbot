from ollama import chat
print("alexa-A chatbot that remember")
messages=[]
messages.append({
    "role":"system",
    "content":"answer in a sentence of around 50 words max"
})
while True:
    question=input("You: ").strip()
    if question.lower()=="exit":
        print("Good bye")
        break
    else:
        messages.append({
        "role":"user",
        "content":question
    })
    response=chat(model="Llama3.2",
    messages=messages)
    answer=response.message.content
    messages.append({
        "role":"assistant",
        "content":answer
    })
    print("Bot: ",answer)