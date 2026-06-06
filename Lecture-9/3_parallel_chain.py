#RunnableParallel : The class that enables parallel execution in LangChain

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model  = ChatOpenAI()
parser = StrOutputParser()

# Template 1 --- Batting info
batting_template = ChatPromptTemplate([
    ("system", "You are a cricket expert"),
    ("human",  "Give batting stats of {player} in 2 lines")
])

# Template 2 --- Bowling info
bowling_template = ChatPromptTemplate([
    ("system", "You are a cricket expert"),
    ("human",  "Give bowling stats of {player} in 2 lines")
])

# Build individual chains
batting_chain = batting_template | model | parser
bowling_chain = bowling_template | model | parser

# Run BOTH simultaneously
parallel_chain = RunnableParallel({
    "batting": batting_chain,
    "bowling": bowling_chain
})

result = parallel_chain.invoke({"player": "Virat Kohli"})

print(result["batting"])
# "Virat Kohli has scored 70+ centuries with average of 58..."

print(result["bowling"])
# "Virat Kohli rarely bowls but has taken occasional wickets..."