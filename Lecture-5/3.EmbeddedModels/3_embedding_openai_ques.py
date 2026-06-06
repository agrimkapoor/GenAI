# we have a document consisting of multiple sentences and we have a query and we want to find the similarity of the query with each sentence of the document. So, we will create embeddings for each sentence of the document and for the query and then we will calculate the cosine similarity between the query embedding and each sentence embedding.


from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

doc_embeddings = embedding.embed_documents(documents) #2d as embeding of many sentences
query_embedding = embedding.embed_query(query) #1d as embedding of single sentence

scores = cosine_similarity([query_embedding], doc_embeddings)[0]
# [query embedding] is 2d 
# so scores is also [[0.45, 0.42, 0.40, 0.43, 0.89]]
scores = scores[0] # to convert it to 1d [0.45, 0.42, 0.40, 0.43, 0.89]

list(enumerate(scores))
# →
[(0, 0.45),   # index 0, Kohli,  score 0.45
 (1, 0.42),   # index 1, Dhoni,  score 0.42
 (2, 0.40),   # index 2, Sachin, score 0.40
 (3, 0.43),   # index 3, Rohit,  score 0.43
 (4, 0.89)]   # index 4, Bumrah, score 0.89
index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1] # sort by score and get the last one which is the highest score

print(query)
# "tell me about bumrah"

print(documents[index])
# documents[4]
# "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."

print("similarity score is:", score)
# "similarity score is: 0.89"