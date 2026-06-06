from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Components
template = ChatPromptTemplate([
    ("system", "You are a cricket expert"),
    ("human",  "Explain {topic} in simple words")
])

model  = ChatOpenAI()
parser = StrOutputParser()

# Connect with pipe
chain = template | model | parser

# Invoke
result = chain.invoke({"topic": "LBW rule"})
print(result)   # "LBW stands for Leg Before Wicket..."


# Reuse for different inputs
result2 = chain.invoke({"topic": "Duckworth Lewis method"})
print(result2)

result3 = chain.invoke({"topic": "powerplay"})
print(result3)