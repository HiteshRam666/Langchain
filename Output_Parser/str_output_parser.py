from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate

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

prompt1 = templat1.invoke({"topic": "Solar system"})

result = model.invoke(prompt1)

prompt2 = template2.invoke({"toptic": result.content})

result1 = model.invoke(prompt2)

print(result1.content)