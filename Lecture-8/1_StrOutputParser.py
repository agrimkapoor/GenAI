from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model  = ChatOpenAI()
parser = StrOutputParser()

template = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    ("human",  "{question}")
])

# Connect with pipe
chain = template | model | parser

result = chain.invoke({"question": "What is cricket?"})

print(type(result))   # <class 'str'>  ← plain string
print(result)         # "Cricket is a bat and ball sport..."