from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

researcher_task = Task(
    description=(
        'Identify the video{topic}.'
        "Get detailed information about the video from the channel"
    ),
    expected_output="A comprehensive 3 paragraph long report based on the {topic} of the video" ,
    tools=[yt_tool],
    agent=blog_researcher
)

write_task= Task(
    description=(
        "Get detailed information from the youtube channel on the topic{topic}"
    ),
    expected_output="Summarise the info from the youtube channel on the topic{topic}" ,
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new_blog-post.md'
)