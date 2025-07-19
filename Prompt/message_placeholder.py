from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder 
from langchain_core.messages import HumanMessage

# Chat Template 
chat_template = ChatPromptTemplate([
    ("system", "You are helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"), 
    ("human", "{query}" )
])

# Load Chat History 
chat_history = [] 
with open("chat_history.txt", 'r') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# Create Prompt 
prompt = chat_template.invoke({
    "chat_history": chat_history, 
    "query": "Where is my refund"
})

print(prompt)