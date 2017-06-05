from flask.views import MethodView
from flask import jsonify
import pymysql.cursors

from Config import Config


class Location(MethodView):
    def get(self):
        self.credentials = CredentialsConfig.shuttleGpsDbCredentials
        return jsonify(ShuttleLocation=self.getCoordinates())

    def multipleshuttles(self):
        self._connect()
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = """select
                        max(id) as id
                    from
                        positions
                    group by deviceid"""

            cursor.execute(sql)
            self.connection.commit()
            idArray = []
            for mostRecentUpdatedIdForEachDevice in cursor.fetchall():
                id = int(mostRecentUpdatedIdForEachDevice['id'])
                idArray.append(id)

            refinedList = ','.join(str(a) for a in idArray)

            sql = """select
                id, latitude, longitude, devicetime, deviceid, servertime
                from positions
                where id in (%s)""" % refinedList

            cursor.execute(sql)
            self.connection.commit()

            locationArray = []

            for location in cursor.fetchall():
                location['updatetime'] = location['servertime']
                del location['servertime']
                del location['devicetime']
                isUpToDate = self._checkIsLastUpdateTimeBiggerThanMinutes(15, location)
                location['isActive'] = not isUpToDate
                locationArray.append(location)

            resultDict = {}
            resultDict['isActive'] = self._isAtLeastOneShuttleActive(locationArray)

            for each in locationArray:
                each['updatetime'] = each['updatetime'].isoformat()

            resultDict['locationArray'] = locationArray
            return resultDict

    def _connect(self):
        self.connection = pymysql.connect(
            user=self.credentials.user,
            password=self.credentials.password,
            host=self.credentials.ip,
            db=self.credentials.dbName,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)

    def _checkIsLastUpdateTimeBiggerThanMinutes(self, minutes, location):
        lastUpdateTime = location['updatetime']
        import datetime
        timeDifference = datetime.datetime.now() - lastUpdateTime
        if (timeDifference.seconds / 60) > minutes:
            return True
        else:
            return False

    def _isAtLeastOneShuttleActive(self, locationArray):
        for each in locationArray:
            if each['isActive'] is True:
                return True
        return False
