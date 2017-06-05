from typing import List

from Helpers.AbstractService import AbstractService
from Services.Phonebook import Phonebook
from Services.Shuttle import Shuttle
from Services.Weather import Weather
from Services.Cafeteria import Cafeteria

class ApiServices:
    def __init__(self):
        self.allServices: List[AbstractService] = []
        self.allServices.append(Weather)
        self.allServices.append(Cafeteria)
        self.allServices.append(Phonebook)
        self.allServices.append(Shuttle)

    def addEndpoints(self, flaskApp):
        for service in self.allServices:
            service(flaskApp).addEndpoints()
