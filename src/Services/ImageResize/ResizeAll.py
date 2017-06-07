from flask.views import MethodView
from flask import jsonify, request

from Services.CafeteriaRate.CafeteriaRating import CafeteriaRating
from Services.ImageResize.ImageProcessor import ImageProcessor


class ResizeAll(MethodView):
    def get(self):
        ImageProcessor().resizeAllStaticPhotos()
        return "200"
