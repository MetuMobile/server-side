from flask.views import MethodView
from flask import jsonify

from Config import Config

class Schedule(MethodView):
    def get(self):
        return jsonify(ShuttleSchedule=self.getWeeklySchedule())

    def getWeeklySchedule(self):
        ShuttleSchedule = []
        for weekDay in range(1, 8):
            ShuttleSchedule.append({'day': weekDay})
            ShuttleSchedule[weekDay-1]['buses'] = DayBusses().getMock(weekDay)

        return ShuttleSchedule


class DayBusses:
    @staticmethod
    def getMock(weekDay):
        dailyBuses = []

        if weekDay <= 7:
            for hour in [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 00]:
                bus = {'index': 0, 'price': 1.0, 'tr_destination': 'ODTU KKK', 'en_destination': 'METU NCC',
                       'stops': [{"hour": hour, "minute": 5, "tr_name": "Terminal", "en_name": "Terminal"},
                                 {"hour": hour, "minute": 10, "tr_name": "Muze", "en_name": "Museum"},
                                 {"hour": hour, "minute": 15, "tr_name": "Kopru Durak", "en_name": "Bridge Stop"},
                                 {"hour": hour, "minute": 20, "tr_name": "ODTU Cemberi", "en_name": "METU Roundabout"},
                                 {"hour": hour, "minute": 25, "tr_name": "Kalkanli", "en_name": "Kalkanli"}]}
                dailyBuses.append(bus)

                bus = {'index': 0, 'price': 1.00, 'tr_destination': 'Terminal', 'en_destination': 'Terminal',
                       'stops': [{"hour": hour, "minute": 45, "tr_name": "2. Yurt", "en_name": "2nd Dormitory"},
                                 {"hour": hour, "minute": 50, "tr_name": "Kalkanli", "en_name": "Kalkanli"},
                                 {"hour": hour, "minute": 55, "tr_name": "ODTU Cemberi", "en_name": "METU Roundabout"},
                                 {"hour": hour + 1, "minute": 0, "tr_name": "Kopru Durak", "en_name": "Bridge Stop"},
                                 {"hour": hour + 1, "minute": 5, "tr_name": "Muze", "en_name": "Museum"}
                                 ]}
                dailyBuses.append(bus)

        return dailyBuses
