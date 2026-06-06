# To create an embedding for a single query  
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)# dimension is the size of the embedding vector 

result = embedding.embed_query("Delhi is the capital of India")

print(result) 
