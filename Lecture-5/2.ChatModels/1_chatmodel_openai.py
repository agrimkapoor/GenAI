from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

result = model.invoke("What is capital of france?")

print(type(result))         # <class 'AIMessage'>
print(result.content)       # result is AIMessage object, to get the actual text content we need to access the .content attribute