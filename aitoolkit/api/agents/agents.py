from flask_restful import Resource, reqparse

from aitoolkit.agents.agent_factory import AgentFactory, get_agent_type
from aitoolkit.api.agents import bp, api


class AgentsAPI(Resource):

    def post(self):
        # parse request
        parser = reqparse.RequestParser()
        parser.add_argument('agent_type', type=str, required=True, location='json')
        parser.add_argument('query', type=str, required=True, location='json')
        args = parser.parse_args()

        # create agent
        agent = AgentFactory[get_agent_type(args['agent_type'])]()

        # query agent
        try:
            response = agent.invoke({'input': args['query']})
            return {
                'result': response['output'],
            }
        except Exception as e:
            return {
                'error': str(e),
            }, 500

# add resource to api
# api.add_resource(AgentsAPI, '/agents', endpoint='agents')
