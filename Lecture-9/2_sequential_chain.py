from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model  = ChatOpenAI()
parser = StrOutputParser()

# Chain 1 --- Generate cricket facts
template1 = ChatPromptTemplate([
    ("system", "You are a cricket expert"),
    ("human",  "Write 3 interesting facts about {player}")
])

# Chain 2 --- Translate to Hindi
template2 = ChatPromptTemplate([
    ("system", "You are a translator"),
    ("human",  "Translate this to Hindi: {text}")
])

# Build sequential chain
chain1 = template1 | model | parser

chain2 = template2 | model | parser

# Connect chain1 output → chain2 input
sequential_chain = chain1 | (lambda x: {"text": x}) | chain2

# x = whatever comes from chain1
# lambda converts it to → {"text": x} which is the expected input for chain2

result = sequential_chain.invoke({"player": "Virat Kohli"})
print(result)
# Hindi translation of cricket facts about Virat Kohli ✅