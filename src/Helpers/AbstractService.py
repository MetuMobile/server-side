from abc import ABC

from flask import Blueprint
from flask import url_for

from Config import Config


class AbstractService(ABC):
    def __init__(self):
        self.serviceName = type(self).__name__.lower()
        self.blueprint = Blueprint(self.serviceName, self.serviceName)
