from Helpers.AbstractService import AbstractService
from Services.ImageResize import ResizeAll


class ImageResize(AbstractService):
    def addEndpoints(self):
        self.addUrl('resizeall', ResizeAll)

        # self.addUrl('meals', ) post a rating
        # def rateCafeteria(mealId):
        #     return CafeteriaRating().rateMenu(mealId)

        # self.addUrl('meals', ) get a rating for meal
        # def showRating(mealId):
        #     return jsonify(mealRating=CafeteriaRating().getMealRating(str(mealId)))


        pass

