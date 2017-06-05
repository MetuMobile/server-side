from abc import ABC, abstractmethod


class AbstractService(ABC):
    def __init__(self, app):
        self.flaskApp = app
        self.serviceName = type(self).__name__.lower()

    @abstractmethod
    def addEndpoints(self):
        pass

    def addUrl(self, inServiceUrl: str, _class):
        endpointPath = '/services/'+str(self.serviceName)+'/'+inServiceUrl+'/'
        self.flaskApp.add_url_rule(endpointPath,
                                   view_func=_class.as_view(endpointPath))
