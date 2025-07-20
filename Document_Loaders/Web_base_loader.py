from langchain_community.document_loaders import WebBaseLoader 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 
load_dotenv() 

model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text -\n {text}", 
    input_variables=["question", "text"]
)

url = "http://amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_4?crid=3HPLUVF5WO38N&dib=eyJ2IjoiMSJ9.mTruFp1_UG2N-c-RoQUkKn6b9LiKcqg-NHxjv99qsD5iv7l-1toJLxfxEMv3FmhUB8O3kErACfga-qUrUmh7suGIemF4H37w0PYwua5CAsnBGHnw1s5Gw57iEX7IpfXElhVsxWACAnKyJ3xO_3TavCynEyPoRtrVBwWicFBopqCQJVSAKrXPIu-8aNgqBlLrBTTWVkQhZvVIT6lh6B46s5xcOf5FcymHMlNU6bbVZxY.2O_JZIHt9f3wZiLRKKUtDFh863wDYVQE7bq2qqU4BO4&dib_tag=se&keywords=mac&qid=1752292754&sprefix=mac%2Caps%2C236&sr=8-4&th=1"
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser 
result = chain.invoke({'question': 'Give the product summary', 'text': docs[0].page_content})
print(result)