from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 
load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

response = llm.invoke("Tell me joke related to Artificial Intelligence")
print(response.content)