from crewai import Crew, Process, LLM
from agents import blog_researcher, blog_writer
from tasks import researcher_task, write_task
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

import os
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    verbose=True,
    google_api_key=google_api_key
)


crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[researcher_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True, 
    llm=llm
)

result = crew.kickoff(inputs={'topic': 'AI vs ML vs DL vs Data Science'})
print(result)