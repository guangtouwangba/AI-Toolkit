from enum import Enum

from aitoolkit.agents.github_search_agent import create_github_search_agent


class AgentType(Enum):
    GithubSearchAgent = 'github_search_agent'


def get_agent_type(agent_type: str) -> AgentType:
    agent_type_map = {
        'github_search_agent': AgentType.GithubSearchAgent
    }
    return agent_type_map[agent_type]


AgentFactory = {
    AgentType.GithubSearchAgent: create_github_search_agent
}
