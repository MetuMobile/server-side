from flask.views import MethodView
from flask import jsonify, request

from Helpers.MongoDatabase import MongoDatabase


class Meals(MethodView):
    def get(self, mealId):
        futureOnly = request.values.get('futureonly')
        if futureOnly=='true' or futureOnly=='True':
            return jsonify(CafeteriaMenu=MongoDatabase().getUpcomingCafeteriaMenu())
        else:
            return jsonify(CafeteriaMenu=MongoDatabase().getAllCafeteriaMenu())
