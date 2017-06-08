from Helpers.AbstractService import AbstractService
from Services.CafeteriaRate.Meals import Meals
from Services.CafeteriaRate.Root import Root


class CafeteriaRate(AbstractService):
    def __init__(self):
        super().__init__()

        mealsView = Meals.as_view('meals')
        self.blueprint.add_url_rule('/meals/<mealId>', view_func=mealsView)
        self.blueprint.add_url_rule('/meals/', defaults={'mealId': None}, view_func=mealsView)

        rootView = Root.as_view('root')
        self.blueprint.add_url_rule('/', view_func=rootView)
