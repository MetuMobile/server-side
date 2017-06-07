
from Helpers.AbstractService import AbstractService
from Services.Weather.DailyForecast import DailyForecast


class Weather(AbstractService):
    def __init__(self):
        super().__init__()

        DailyForecastView = DailyForecast.as_view('dailyforecast')
        self.blueprint.add_url_rule('/', view_func=DailyForecastView)

