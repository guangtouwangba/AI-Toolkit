from datetime import datetime
from typing import Any, Type

import dotenv
import requests
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

dotenv.load_dotenv()


class GithubToolInput(BaseModel):
    query: str = Field(description="search query to look up")
    top_n: int = Field(description="number of top results to return")


class GitRepoSearchTool(BaseTool):
    name: str = "git_repo_search"
    description: str = "Search for github repositories"
    version: str = "0.1.0"
    args_schema: Type[BaseModel] = GithubToolInput
    api_version: str = "2022-11-28"
    access_tokens: str = ""

    def _run(self, query, top_n) -> Any:
        headers = {
            "Content-Type": "application/vnd.github+json",
            "Authorization": f"Bearer {self.access_tokens}",
            "X-GitHub-Api-Version": self.api_version,
        }
        api_domain = 'https://api.github.com'
        response = requests.get(
            url=f"{api_domain}/search/repositories?q={query}&sort=stars&per_page={top_n}&order=desc",
            headers=headers,
        )
        response_data = response.json()
        if response.status_code == 200 and isinstance(response_data.get('items'), list):
            contents = list()
            if len(response_data.get('items')) > 0:
                for item in response_data.get('items'):
                    content = dict()
                    updated_at_object = datetime.strptime(item['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
                    content['owner'] = item['owner']['login']
                    content['name'] = item['name']
                    content['description'] = item['description'][:100] + '...' if len(item['description']) > 100 else \
                        item['description']
                    content['url'] = item['html_url']
                    content['star'] = item['watchers']
                    content['forks'] = item['forks']
                    content['updated'] = updated_at_object.strftime("%Y-%m-%d")
                    contents.append(content)
                print(contents)
                return " ".join(
                    [f"{content['name']} - {content['description']} - {content['url']}" for content in contents])

            else:
                return f'No items related to {self.query} were found.'
        else:
            return response.json().get('message')

