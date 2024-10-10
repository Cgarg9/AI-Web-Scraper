from crewai import Agent 

# senior blog content researcher

blog_researcher = Agent(
    role="blog researcher from youtube videos",
    goal="get the relevant video content for the topic{topic} from youtube channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, ML and GenAI and providing suggestions"
    ),
    tool=[],
    allow_delegation=True
)

# senior blog writer agent 
