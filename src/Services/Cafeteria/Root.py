from flask.views import MethodView
from flask import jsonify
from Helpers.EndpointList import EndpointList



class Root(MethodView):
    def get(self):
        return jsonify(Endpoints=self.getEndpoints())

    def getEndpoints(self):
        endpoints = EndpointList('cafeteria')
        endpoints.newEndpoint('meals')
        endpoints.newEndpoint('mealImportExcelFileRefresh')
        endpoints.newEndpoint('WebMenuUploader')

        return endpoints.getEndpointHrefs()
