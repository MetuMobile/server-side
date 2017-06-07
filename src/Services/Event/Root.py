from flask.views import MethodView
from flask import jsonify
from Helpers.EndpointList import EndpointList



class Root(MethodView):
    def get(self):
        return jsonify(Endpoints=self.getEndpoints())

    def getEndpoints(self):
        endpoints = EndpointList('event')
        endpoints.newEndpoint('upcoming')

        return endpoints.getEndpointHrefs()
