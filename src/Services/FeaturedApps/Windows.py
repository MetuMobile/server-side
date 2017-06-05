from flask.views import MethodView
from flask import jsonify


class Windows(MethodView):
    def get(self):
        return jsonify(FeaturedApps=self.getFeaturedApps())

    def getFeaturedApps(self):
        links = [
            {
                "en_appName": "Radio ODTU Northern Cyprus Studios",
                "tr_appName": "Radyo ODTU Kuzey Kıbrıs Stüdyoları",
                "storeLink": "https://www.microsoft.com/en-us/store/p/radyo-odtu-k%C4%B1br%C4%B1s/9nblggh52pwh"
            }
        ]
        return links
