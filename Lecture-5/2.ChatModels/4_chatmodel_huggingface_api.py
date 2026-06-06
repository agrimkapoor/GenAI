from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Step 1 --- Create HuggingFaceEndpoint (the base LLM)
llm = HuggingFaceEndpoint(
    repo_id='tiiuae/falcon-7b-instruct',   
    task='text-generation',
    temperature=0.5,                        # ✅ here
    max_new_tokens=100                      # ✅ correct param name
)

# Step 2 --- Wrap with ChatHuggingFace (chat interface)
model = ChatHuggingFace(llm=llm)           # ✅ llm not model

# Step 3 --- Invoke
result = model.invoke("What is the capital of France?")

print(result.content)