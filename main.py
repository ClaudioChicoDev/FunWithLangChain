import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


# Load environment variables from .env file
load_dotenv('.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI API
llm = OpenAI(openai_api_key="OPENAI_API_KEY")

# Setup llm parameters
llm = OpenAI(temperature=0.9)

# Prompt template
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

while True:
    # Get input from user
    user_input = input("\nWhat product does your company make? (Type 'exit' to quit): ")

    # Exit if user types 'exit'
    if user_input.lower().strip() == "exit":
        break

    # Generate company name
    company_name = llm(prompt.format(product=user_input))

    # Print company name
    print(f"Company name: {company_name}\n")

print("\nGoodbye!")
