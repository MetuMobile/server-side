from flask.views import MethodView
from flask import jsonify


class Ios(MethodView):
    def get(self):
        return jsonify(FeaturedApps=self.getFeaturedApps())

    def getFeaturedApps(self):
        links = [
            {
                "en_appName": "Radio ODTU Northern Cyprus Studios",
                "tr_appName": "Radyo ODTU Kuzey Kıbrıs Stüdyoları",
                "storeLink": "https://itunes.apple.com/tr/app/radyo-odtu-kks/id1126479317"
            }
        ]
        return links
