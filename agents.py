from crewai import Agent 
from tools import yt_tool

# senior blog content researcher

blog_researcher = Agent(
    role="blog researcher from youtube videos",
    goal="get the relevant video content for the topic{topic} from youtube channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, ML and GenAI and providing suggestions"
    ),
    tools=[yt_tool],
    allow_delegation=True
)

# senior blog writer agent 

blog_writer = Agent(
    role="Blog writer",
    goal="Narrate compelling tech stories about the video{topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False
)