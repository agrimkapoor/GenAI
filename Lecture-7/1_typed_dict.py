from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

#Step1 : Define structure  
class Person(TypedDict):
    name: str
    age: int
    country: str

# Step 2 --- Create model with structured output
model = ChatOpenAI()
structured_model = model.with_structured_output(Person)

result = structured_model.invoke("Tell me about Virat Kohli")


print(type(result))   # <class 'dict'>
print(result) # returns a python dictionary 

print(result["name"])    # "Virat Kohli"
print(result["age"])     # 35
print(result["country"]) # "India"