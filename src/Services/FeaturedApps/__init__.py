from Helpers.AbstractService import AbstractService
from Services.FeaturedApps.Android import Android
from Services.FeaturedApps.Ios import Ios
from Services.FeaturedApps.Windows import Windows


class FeaturedApps(AbstractService):
    def addEndpoints(self):
        self.addUrl('android', Android)
        self.addUrl('ios', Ios)
        self.addUrl('windows', Windows)
