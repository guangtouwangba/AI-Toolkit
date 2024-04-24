import os

from langchain import hub
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_community.chat_models import ChatOpenAI

from aitoolkit.tools.github.github_search import GitRepoSearchTool
import dotenv

dotenv.load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")


def create_github_search_agent():
    tool = GitRepoSearchTool()
    tool.access_tokens = github_token
    llm = ChatOpenAI(temperature=0, model="gpt-4-turbo")
    prompt = hub.pull("hwchase17/openai-functions-agent")

    agent = create_openai_functions_agent(
        llm=llm,
        tools=[tool],
        prompt=prompt,
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=[tool],
        verbose=True,
    )

    return agent_executor
