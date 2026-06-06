from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
# this is new import, not from langchain_core but from langchain package directly 
from dotenv import load_dotenv

load_dotenv()

# Step 1 --- Define fields using ResponseSchema
response_schemas = [
    ResponseSchema(
        name="name",
        description="Full name of the cricket player"
    ),
    ResponseSchema(
        name="age",
        description="Current age of the player as integer"
    ),
    ResponseSchema(
        name="country",
        description="Country the player represents"
    ),
    ResponseSchema(
        name="centuries",
        description="Total number of international centuries scored"
    ),
    ResponseSchema(
        name="role",
        description="Player role: batsman, bowler, allrounder or wicketkeeper"
    )
]

# Step 2 --- Create parser
parser = StructuredOutputParser.from_response_schemas(response_schemas)

# Step 3 --- Get format instructions
format_instructions = parser.get_format_instructions()
print(format_instructions)
# Output →
# The output should be a markdown code snippet formatted
# in the following schema, including the leading and
# trailing "```json" and "```":
#
# ```json
# {
#   "name": string  // Full name of the cricket player
#   "age": string   // Current age of the player
#   "country": string // Country the player represents
#   "centuries": string // Total centuries scored
#   "role": string  // Player role
# }
# ```

# Step 4 --- Create template
template = ChatPromptTemplate([
    ("system", """You are a cricket expert.
                  {format_instructions}"""),
    ("human",  "Tell me about {player}")
])

# Step 5 --- Create chain
model = ChatOpenAI()
chain = template | model | parser

# Step 6 --- Invoke
result = chain.invoke({
    "player": "Virat Kohli",
    "format_instructions": format_instructions
})

# Step 7 --- Access
print(type(result))          # <class 'dict'>
print(result)
# {
#   "name":     "Virat Kohli",
#   "age":      "35",
#   "country":  "India",
#   "centuries":"70",
#   "role":     "batsman"
# }

print(result["name"])        # "Virat Kohli"
print(result["age"])         # "35"
print(result["country"])     # "India"
print(result["centuries"])   # "70"
print(result["role"])        # "batsman"