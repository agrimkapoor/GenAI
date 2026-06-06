from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

template = ChatPromptTemplate([
    ("system",  "You are a helpful assistant"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human",   "{question}")
])

model = ChatOpenAI()
chain = template | model

# Turn 1 --- no history
result = chain.invoke({
    "chat_history": [],
    "question":     "My name is Raj"
})
print(result.content)
# "Hello Raj! How can I help?"

