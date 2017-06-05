from flask.views import MethodView
from flask import jsonify


class Android(MethodView):
    def get(self):
        return jsonify(FeaturedApps=self.getFeaturedApps())

    def getFeaturedApps(self):
        links = [
            {
                "en_appName": "Radio ODTU Northern Cyprus Studios",
                "tr_appName": "Radyo ODTU Kuzey Kıbrıs Stüdyoları",
                "storeLink": "https://play.google.com/store/apps/details?id=com.tanss.radyoodtukks"
            }
        ]
        return links
