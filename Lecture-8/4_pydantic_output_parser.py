from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

# Step 1 --- Define Pydantic Model
class Person(BaseModel):
    name:    str = Field(description="Full name of person")
    age:     int = Field(description="Age of person")
    country: str = Field(description="Country of person")

# Step 2 --- Create Parser
parser = PydanticOutputParser(pydantic_object=Person)

# Step 3 --- Get Format Instructions
format_instructions = parser.get_format_instructions()

# Step 4 --- Create Template
template = ChatPromptTemplate([
    ("system", """You are a helpful assistant.
                  {format_instructions}"""),
    ("human",  "Tell me about {name}")
])

# Step 5 --- Build Chain
model = ChatOpenAI()
chain = template | model | parser

# Step 6 --- Invoke
result = chain.invoke({
    "name": "Virat Kohli",
    "format_instructions": format_instructions
})

# Step 7 --- Access Fields
print(type(result))      # <class 'Person'>
print(result)            # Person(name='Virat Kohli', age=35, country='India')
print(result.name)       # "Virat Kohli"
print(result.age)        # 35   ← integer 
print(result.country)    # "India"