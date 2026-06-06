# prompt template : it is for creating dynamic prompts for llm 
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

template = PromptTemplate(
    template="Write a {adjective} poem about {topic}",
    input_variables=["adjective", "topic"]
)

prompt = template.invoke({
    "adjective": "beautiful", 
    "topic": "cricket"
})

print(prompt)

model = OpenAI()
result = model.invoke(prompt)
print(result)