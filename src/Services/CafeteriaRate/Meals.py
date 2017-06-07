from flask.views import MethodView
from flask import jsonify, request

from Services.CafeteriaRate.CafeteriaRating import CafeteriaRating


class Meals(MethodView):
    def get(self, mealId):
        try:
            expandforexcelexport = request.values.get('expandforexcelexport') in ['True', 'true', '1']
        except:
            expandforexcelexport = False
        if mealId:
            mealRating = CafeteriaRating().getMealRating(mealId)
            result = jsonify(mealRating = mealRating)
        else:
            mealRatings = CafeteriaRating().getMealRating()
            if expandforexcelexport:
                mealRatings = self._expandRatingsWithMeal(mealRatings)
                for mealRating in mealRatings:
                    mealRating['numberOfRates'] = CafeteriaRating().getMealRateCount(mealId = mealRating['_id'])
            result = jsonify(mealRatings = mealRatings)
        return result

    def post(self, mealId):
        return CafeteriaRating().rateMenu(mealId)

    def _expandRatingsWithMeal(self, mealRatings):
        for meal in mealRatings:
            mealId = meal['_id']

            import json
            from urllib.request import urlopen
            from Config import Config
            url = Config.cafeteriaServiceUrl + "/meals/"+mealId
            response = urlopen(url).read()
            jsonEndpointData = json.loads(response)
            mealDetails = jsonEndpointData
            meal['tr_name'] = mealDetails['tr_name']
            meal['dishes.main.tr_name'] = mealDetails['dishes']['main']['tr_name']
            meal['dishes.side.tr_name'] = mealDetails['dishes']['side']['tr_name']
            meal['dishes.soup.tr_name'] = mealDetails['dishes']['soup']['tr_name']

        return mealRatings