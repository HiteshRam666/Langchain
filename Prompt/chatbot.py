from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv() 

model = ChatOpenAI() 

chat_history = [
    SystemMessage("You are a helpful assistant")
]

while True:
    user_input = input("You: ", )
    chat_history.append(HumanMessage(content=user_input)) 
    if user_input == "exit":
        break
    result = model.invoke(user_input) 
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)