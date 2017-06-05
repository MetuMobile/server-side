from flask.views import MethodView
from flask import jsonify
from Services.Event.MetuEventsDb import MetuEventsDb


class UpcomingRaw(MethodView):
    def get(self):
        return jsonify(RawUpcomingEvents=self.getRawUpcomingEvents())

    def getRawUpcomingEvents(self):
        db = MetuEventsDb()
        events = db.fetchAllRaw()
        db.connection.close()

        return events

    def _isLongerThan6Months(self, event):
        firstDate = event['ilk_tarih']
        lastDate = event['son_tarih']
        delta = lastDate - firstDate
        return True if delta.days>180 else False
