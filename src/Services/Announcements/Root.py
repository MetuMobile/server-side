from flask.views import MethodView
from flask import jsonify

from Config import Config
from Services.Announcements.MetuAnnouncementsBridge import MetuAcademicAndDormCalendarBridge


class Root(MethodView):
    def get(self):
        return jsonify(Announcements=self.getAnnouncements())

    def getAnnouncements(self):
        announcements = {}
        announcements['academic'] = self._fetchStaticAnnouncementCategory(0)
        announcements['dorm'] = self._fetchStaticAnnouncementCategory(1)
        return announcements

    def _fetchStaticAnnouncementCategory(self, categoryId):
        if categoryId == 0:
            answerDictionary = {}
            answerDictionary['announcements'] = MetuAcademicAndDormCalendarBridge().fetchAcademicAnnouncements()
            answerDictionary['isActive'] = True
            answerDictionary['en_name'] = "Academic"
            answerDictionary['tr_name'] = "Akademik"
        elif categoryId == 1:
            answerDictionary = {}
            answerDictionary['announcements'] = MetuAcademicAndDormCalendarBridge().fetchDormAnnouncements()
            answerDictionary['isActive'] = True
            answerDictionary['en_name'] = "Dormitories"
            answerDictionary['tr_name'] = "Yurtlar"
