
from Helpers.AbstractService import AbstractService
from Services.Weather.DailyForecast import DailyForecast


class Weather(AbstractService):
    def addEndpoints(self):
        self.addUrl('dailyforecast', DailyForecast)
