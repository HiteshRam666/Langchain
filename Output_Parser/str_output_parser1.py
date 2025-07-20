from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

# 1st prompt -> Detailed Report 
templat1 = PromptTemplate(
    template="Write a detailed topic on {topic}", 
    input_variables=["topic"]
)

# 2nd Prompt -> Summary
template2 = PromptTemplate(
    template="Write a 5 line summary report on the following {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = templat1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'solar system'})
print(result)