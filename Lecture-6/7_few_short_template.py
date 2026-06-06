from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Step 1 --- Define examples
examples = [
    {
        "input":  "I love playing cricket",
        "output": "positive"
    },
    {
        "input":  "Cricket match was cancelled",
        "output": "negative"
    },
    {
        "input":  "The weather is okay today",
        "output": "neutral"
    }
]

# Step 2 --- Define example template
example_template = ChatPromptTemplate([
    ("human", "{input}"),
    ("ai",    "{output}")
])

# Step 3 --- Create FewShot template
few_shot_template = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_template
)

# Step 4 --- Full template with few shot examples
final_template = ChatPromptTemplate([
    ("system", "You are a sentiment classifier. Classify as positive, negative or neutral."),
    few_shot_template,      # ← examples injected here
    ("human", "{input}")    # ← actual question
])

# Step 5 --- Create chain
model  = ChatOpenAI()
parser = StrOutputParser()

chain = final_template | model | parser

# Test
result = chain.invoke({"input": "I really enjoyed watching the cricket match!"})
print(result)