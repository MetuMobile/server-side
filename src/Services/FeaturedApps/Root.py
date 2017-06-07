from flask.views import MethodView
from flask import jsonify
from Helpers.EndpointList import EndpointList



class Root(MethodView):
    def get(self, serviceName):
        return jsonify(Endpoints=self.getEndpoints(serviceName))

    def getEndpoints(self, serviceName):
        endpoints = EndpointList(serviceName)
        endpoints.newEndpoint('android')
        endpoints.newEndpoint('ios')
        endpoints.newEndpoint('windows')

        return endpoints.getEndpointHrefs()
