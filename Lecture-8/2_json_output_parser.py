from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model  = ChatOpenAI()
parser = JsonOutputParser()

template = ChatPromptTemplate([
    ("system", """You are a helpful assistant.
                  Always respond in valid JSON format only.
                  No extra text, just JSON."""),
    ("human",  "Give me details about cricket player: {player}")
])

chain = template | model | parser

result = chain.invoke({"player": "Virat Kohli"})

print(type(result))          # <class 'dict'>
print(result)
print(result["name"])
print(result["age"])