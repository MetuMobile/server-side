from flask import url_for

from Config import Config


class EndpointList:
    def __init__(self, serviceName):
        self.endpointNames = []
        self.serviceName = serviceName

    def getEndpointHrefs(self):
        result = []
        for url in self.endpointNames:
            result.append({'href': Config.serverRootLink + url_for(url)})
        return result

    def newEndpoint(self, endpointName):
        self.endpointNames.append(self.serviceName+'.'+endpointName)
