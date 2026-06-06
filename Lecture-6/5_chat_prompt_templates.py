from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Using message objects directly
template = ChatPromptTemplate([
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about {topic}")
])

model = ChatOpenAI()
chain = template | model

result = chain.invoke({"topic": "cricket"})
print(result.content)