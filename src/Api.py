from flask import jsonify
from flask.views import MethodView
from Config import Config

class Api(MethodView):
    def __init__(self):
        pass

    def get(self):
        return jsonify(Response = {
            'version' : Config.serverVersion,
            'masterCache' : 'TODO',
            'services': {
                'href': Config.serverRootLink + Config.apiRootLink + '/services'
            }
        })
