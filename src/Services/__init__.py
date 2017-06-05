from typing import List

from Helpers.AbstractService import AbstractService
from Services.Event import Event
from Services.FeaturedApps import FeaturedApps
from Services.Phonebook import Phonebook
from Services.Shuttle import Shuttle
from Services.Weather import Weather
from Services.Cafeteria import Cafeteria

class ApiServices:
    def __init__(self):
        self.allServices: List[AbstractService] = []
        self.allServices.append(Cafeteria)
        self.allServices.append(Event)
        self.allServices.append(FeaturedApps)
        self.allServices.append(Phonebook)
        self.allServices.append(Shuttle)
        self.allServices.append(Weather)

    def addEndpoints(self, flaskApp):
        for service in self.allServices:
            service(flaskApp).addEndpoints()
