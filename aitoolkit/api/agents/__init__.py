from flask import Blueprint
from flask_restful import Api

from aitoolkit.api.external_api import ExternalApi

bp = Blueprint('agents', __name__, url_prefix='/v1')

api = Api(bp)

# api = ExternalApi(bp)
