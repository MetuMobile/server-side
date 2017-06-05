from flask.views import MethodView
from flask import jsonify

from Config import Config


class PhonebookContents(MethodView):
    def get(self):
        return jsonify(Phonebook=self.getPhonebook())

    def __init__(self):
        if Config.debug:
            self.phonebookBridge = MockPhonebookBridge()
        else:
            self.phonebookBridge = PhonebookBridge()
        pass

    def getPhonebook(self):
        rawDbResult = self.phonebookBridge.fetchAllFromDb()
        activePhonebookRecords = []
        for eachRecord in rawDbResult:
            if eachRecord['durum'] == "aktif":
                recordDict = {}
                recordDict['title'] = eachRecord['title']
                recordDict['pinned'] = False
                name = eachRecord['name']
                if name[0] == " " or name[0] == "!":
                    name = name[1:]
                    recordDict['pinned'] = True
                recordDict['name'] = name
                recordDict['surname'] = eachRecord['surname']
                recordDict['position'] = eachRecord['position']
                recordDict['officeTel'] = eachRecord['oftelno']
                recordDict['unit'] = eachRecord['unit']
                recordDict['officeLocation'] = eachRecord['ofno']
                try:
                    recordDict['email'] = str(eachRecord['email']) + "@metu.edu.tr"
                except:
                    recordDict['email'] = None
                activePhonebookRecords.append(recordDict)
        return activePhonebookRecords


class PhonebookBridge:
    def __init__(self):
        from CredentialsConfig import CredentialsConfig
        self.credentials = CredentialsConfig.phonebookDbCredentials
        pass

    def _connect(self):
        import pymysql.cursors
        self.connection = pymysql.connect(
            user=self.credentials.user,
            password=self.credentials.password,
            host=self.credentials.ip,
            db=self.credentials.dbName,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)

    def fetchAllFromDb(self):
        self._connect()
        with self.connection.cursor() as cursor:
            sql = """select *
              from rehber
              ORDER BY name ASC"""
            #where durum not like '%pasif%'"""
            cursor.execute(sql)
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()
            result = cursor.fetchall()
            return result




class MockPhonebookBridge:
    def fetchAllFromDb(self):
        return [
            {
                'durum':'aktif',
                'oftelno':'oftelno',
                'unit':'unit',
                'ofno':'ofno',
                'position':'position',
                'surname':'surname',
                'name':' name',
                'title':'title',
                'surname':'aktif',
                'email':'email',
            },
            {
                'durum':'pasif',
                'oftelno':'oftelno',
                'unit':'unit',
                'ofno':'ofno',
                'position':'position',
                'surname':'surname',
                'name':'name',
                'title':'title',
                'surname':'aktif',
                'email':'email',
            },
            {
                'durum':'aktif',
                'oftelno':'oftelno',
                'unit':'unit',
                'ofno':'ofno',
                'position':'position',
                'surname':'surname',
                'name':'name',
                'title':'title',
                'surname':'aktif',
                'email':'email',
            },
        ]