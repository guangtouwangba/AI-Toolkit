from aitoolkit.api.agents.agents import AgentsAPI


def initialize_router(api):
    api.add_resource(AgentsAPI, '/v1/agents', endpoint='agents')
