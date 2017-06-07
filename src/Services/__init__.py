from flask import jsonify
from flask.views import MethodView
from Config import Config

class ApiServices(MethodView):
    def __init__(self):
        self.endpointNames = []

    def get(self, servicelist):
        for service in servicelist:
            self.endpointNames.append({'href': Config.serverRootLink + Config.apiRootLink +'/services/'+
                                               service.__name__.lower()})
        return jsonify(Services = self.endpointNames)
