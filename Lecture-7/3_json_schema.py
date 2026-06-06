from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Define JSON schema
json_schema = {
    "title": "CricketPlayer",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Full name of the player"
        },
        "age": {
            "type": "integer",
            "description": "Age of the player"
        },
        "country": {
            "type": "string",
            "description": "Country represented"
        },
        "centuries": {
            "type": "integer",
            "description": "Total international centuries"
        }
    },
    "required": ["name", "age", "country", "centuries"]
}

model = ChatOpenAI()
structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("Tell me about Sachin Tendulkar")

print(type(result))         # <class 'dict'>
print(result)
# {
#   "name": "Sachin Tendulkar",
#   "age": 50,
#   "country": "India",
#   "centuries": 100
# }

print(result["name"])       # "Sachin Tendulkar"
print(result["centuries"])  # 100