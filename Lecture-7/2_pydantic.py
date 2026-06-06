from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# Step 1 --- Define structure
class Person(BaseModel):
    name:    str
    age:     int
    country: str

# Step 2 --- Create structured model
model = ChatOpenAI()
structured_model = model.with_structured_output(Person)

# Step 3 --- Invoke
result = structured_model.invoke("Tell me about Virat Kohli")

# Step 4 --- Access like object
print(type(result))         # <class 'Person'>
print(result)
# Person(name='Virat Kohli', age=35, country='India')

print(result.name)          # "Virat Kohli"
print(result.age)           # 35
print(result.country)       # "India"