from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv

load_dotenv()

import os
os.environ["GROQ_API_KEY"] =" mn jkn "
os.environ["GROQ_MODEL_NAME"]="groq/llama-3.2-90b-text-preview"

## Create a senior blog content researcher

blog_researcher=Agent(
    role='Blog Researcher from Website',
    goal='get the relevant website data/information for the topic {topic} from the provided Website',
    verboe=True,
    memory=True,
    backstory=(
       "Expert in understanding Websited in Automobiles, cars bikes etc and providing suggestion" 
    ),
    tools=[yt_tool],
    allow_delegation=True
)

## creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Explain the topic {topic} in a simple and engaging manner for drivers and technicicans to understand',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False


)
