from Helpers.AbstractService import AbstractService
from Services.Shuttle.Location import Location
from Services.Shuttle.Schedule import Schedule


class Shuttle(AbstractService):
    def addEndpoints(self):
        self.addUrl('schedule', Schedule)
        self.addUrl('location', Location)
