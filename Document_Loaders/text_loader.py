from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv 
load_dotenv() 

model = ChatOpenAI()

prompt = PromptTemplate(
    template="Write a summary for following {poem}", 
    input_variables=["poem"]
)

parser = StrOutputParser()

loader = TextLoader("Document_Loaders\\cricket.txt", encoding = "utf-8")

docs = loader.load()

# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | model | parser 

result = chain.invoke({'poem': docs[0].page_content})

print(result)