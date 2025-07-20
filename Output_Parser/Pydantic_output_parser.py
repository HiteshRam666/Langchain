from pydantic import BaseModel, Field 
from langchain_core.output_parsers import PydanticOutputParser 
from langchain_core.prompts import PromptTemplate 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI 

load_dotenv() 

model = ChatOpenAI() 

class Person(BaseModel):
    
    name: str = Field(description="Name of the person") 
    age: int = Field(description="Age of the person")
    city: str = Field(description="Name of city the person belongs too") 

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age, city of the fiction {place} person \n {format_instructions}",
    input_variables=["place"], 
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

# prompt = template.invoke({'place': 'indian'})

# result = model.invoke(prompt) 

# final_result = parser.parse(result.content) 

chain = template | model | parser

final_result = chain.invoke({'place': 'indian'})

# print(final_result)
print(final_result)