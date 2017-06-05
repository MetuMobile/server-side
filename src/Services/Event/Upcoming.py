from flask.views import MethodView
from flask import jsonify
from datetime import datetime

from Services.Event.MetuEventsDb import MetuEventsDb


class Upcoming(MethodView):
    def get(self):
        return jsonify(UpcomingEvents=self.getUpcomingEvents())

    def getUpcomingEvents(self):
        db = MetuEventsDb()
        events = db.fetchAll()
        db.connection.close()

        upcomingEvents = []
        for event in events:
            del event["event_category"]
            del event["event_status"]
            del event["status"]
            #http://ncc.metu.edu.tr/sites/default/files/etkinlik-dugunumuz-var.jpg
            event["image_uri"] = event["image_uri"].replace("public://", "http://ncc.metu.edu.tr/sites/default/files/")

            if self._isLongerThan6Months(event):
                continue

            if event["son_tarih"] >= datetime.today():
                event["ilk_tarih"] = event["ilk_tarih"].isoformat()
                event["son_tarih"] = event["son_tarih"].isoformat()
                upcomingEvents.append(event)

        return upcomingEvents

    def _isLongerThan6Months(self, event):
        firstDate = event['ilk_tarih']
        lastDate = event['son_tarih']
        delta = lastDate - firstDate
        return True if delta.days>180 else False
