from langchain_community.document_loaders import CSVLoader
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 
load_dotenv() 

model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template="Analyse the docs and give summary- {document}", 
    input_variables=["summary"]
)

loader = CSVLoader("Document_Loaders\\Social_Network_Ads.csv")

docs = loader.load()

# print(len(docs))
# print(docs[0])
chains = prompt | model | parser 
result = chains.invoke({'document': docs[0]})
print(result)
# results = [chains.invoke({'document': doc.page_content}) for doc in docs]
# for i, result in enumerate(results):
#     print(f"\n--- Document {i+1} Summary ---")
#     print(result)
#     break