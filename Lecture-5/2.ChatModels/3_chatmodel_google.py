from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()   
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.5, max_output_tokens=100)
result = model.invoke("What is the capital of France?") 
print(result.content)