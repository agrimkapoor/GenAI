#ChatPromptTemplate ,MessagesPlaceholder ,FewShotPromptTemplate  
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    FewShotChatMessagePromptTemplate
)
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Few shot examples
examples = [
    {"input": "2+2",   "output": "4"},
    {"input": "5X5",   "output": "25"},
    {"input": "10-3",  "output": "7"}
]

example_template = ChatPromptTemplate([
    ("human", "{input}"),
    ("ai",    "{output}")
])

few_shot = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_template
)

# Full template
template = ChatPromptTemplate([
    ("system", "You are a math expert. Give only the answer."),
    few_shot,
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

model  = ChatOpenAI()
parser = StrOutputParser()

chain = template | model | parser

chat_history = []

# Use the chain
result = chain.invoke({
    "chat_history": chat_history,
    "question":     "15+15"
})
print(result) 

# Update history
chat_history.append(HumanMessage(content="15+15"))
chat_history.append(AIMessage(content=result))

result = chain.invoke({
    "chat_history": chat_history,
    "question":     "What was my first question?"
})
print(result) 