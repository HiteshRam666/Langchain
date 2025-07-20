from langchain_community.document_loaders import PyPDFLoader 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 
load_dotenv() 

model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template="Give summary of the {document}", 
    input_variables=["document"]
)

loader = PyPDFLoader("Document_Loaders\\Attention.pdf")

docs = loader.load()

# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | model | parser 

result = chain.invoke({'document': docs[0].page_content})
print(result)