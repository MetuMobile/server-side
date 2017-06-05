from Helpers.AbstractService import AbstractService
from Services.Event.Upcoming import Upcoming
from Services.Event.UpcomingRaw import UpcomingRaw


class Event(AbstractService):
    def addEndpoints(self):
        self.addUrl('upcoming', Upcoming)
        self.addUrl('upcomingraw', UpcomingRaw)
