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
    elif question.lower() == "history":
        print("\n----Chat History----")
        for message in messages:
            if message["role"]=="user":
                print("You: ",message["content"])
            elif message["role"]=="assistant":
                print("Bot: ",message["content"])
            print("-------------------------\n")
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