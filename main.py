import os
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

# Load environment variables from .env file
load_dotenv('.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI API
llm = OpenAI(openai_api_key="OPENAI_API_KEY")

# Setup llm parameters
llm = OpenAI(temperature=0.1)

# Load some tools
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

# Initialize agent with the tools
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Now let's test it out!
agent.run("what is 469219 Kamoʻoalewa? How big is it and what is it made of?")
