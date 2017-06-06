from Helpers.AbstractService import AbstractService
from Services.Announcements.AllAnnouncements import AllAnnouncements


class Announcements(AbstractService):
    def addEndpoints(self):
        self.addUrl('all', AllAnnouncements)
