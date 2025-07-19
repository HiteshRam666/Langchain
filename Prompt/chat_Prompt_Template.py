# from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', "You are helpful {domain} expert"), 
    ('human', "Explain in simple term, What is {topic}")
    # SystemMessage(content="You are helpful {domain} expert"), 
    # HumanMessage(content="Explain in simple term, What is {topic}")
])

prompt = chat_template.invoke({'domain': 'Computer science', 'topic': 'Operating System'})

print(prompt)