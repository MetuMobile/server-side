from Helpers.AbstractService import AbstractService
from Services.Booklet.Booklets import Booklets


class Booklet(AbstractService):
    def addEndpoints(self):
        self.addUrl('booklets', Booklets)
