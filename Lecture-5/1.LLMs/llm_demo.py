from langchain_openai import OpenAI # from the installed package, import the OpenAI LLM class
from dotenv import load_dotenv
load_dotenv() # load environment variables from the .env file which should contain the OPENAI_API_KEY


model = OpenAI(
    model="gpt-3.5-turbo-instruct",   # default
    temperature=0.7,                   # default
    max_tokens=256                     # default
) # create an instance of the OpenAI LLM.

#temperature is a parameter that controls the randomness of the output. its range is [0.0 to 2.0] .where 0 is deterministic and 2 is very random. 

# max completion tokens is the maximum number of tokens that the model can generate in response to a prompt. token is basic unit of text that the model processes. token can be assumed to be roughly equivalent to a word 
result = model.invoke("What is LangChain?")# invoke the model with a prompt and store the result

print(type(result))   # <class 'str'>
print(result) # result is a string (plain text)

