from flask import Flask
import sys
from Config import Config
# from Services import Services
from Services import Announcements
from Services import Cafeteria
from Services.Booklet import Booklet

class Server:
    def __init__(self):
        sys.stdout.flush()
        self.app = Flask(__name__)
        self.app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
        self._addLogger()
        self.services = []

    def _addLogger(self):
        import logging
        handler = logging.FileHandler(Config.loggerPath)  # errors logged to this file
        handler.setLevel(logging.ERROR)  # only log errors and above
        self.app.logger.addHandler(handler)  # attach the handler to the app's logger

    def run(self):
        self.app.run(debug=Config.debug, host='0.0.0.0', port=Config.serverPort, threaded=True)
        print("api service is started.")

    def addUrlRules(self):
        # https://ip:url/api/v1/
        self.services.append(Announcements)
        self.services.append(Booklet)
        self.services.append(Cafeteria)

        self._addBlueprintsOfServices()

    def _addBlueprintsOfServices(self):
        for serviceClass in self.services:
            serviceInstance = serviceClass()
            self.app.register_blueprint(serviceInstance.blueprint,
                                        url_prefix= Config.apiRootLink + '/services/' + serviceInstance.serviceName)


if __name__ == "__main__":
    server = Server()
    server.addUrlRules()
    server.run()
