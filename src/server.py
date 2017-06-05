from flask import Flask
import sys
from Config import Config
from Services import ApiServices

class Server:
    def __init__(self):
        self._initializeService()

    def _addLogger(self):
        import logging
        handler = logging.FileHandler(Config.loggerPath)  # errors logged to this file
        handler.setLevel(logging.ERROR)  # only log errors and above
        self.app.logger.addHandler(handler)  # attach the handler to the app's logger

    def _initializeService(self):
        sys.stdout.flush()
        self.app = Flask(__name__)
        self.app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
        self._addLogger()

    def run(self):
        self.app.run(debug=Config.debug, host='0.0.0.0', port=Config.serverPort, threaded=True)
        print("api service is started.")

    def addUrlRules(self):
        # https://ip:url/api/v1/
        ApiServices().addEndpoints(self.app)


if __name__ == "__main__":
    server = Server()
    server.addUrlRules()
    server.run()
