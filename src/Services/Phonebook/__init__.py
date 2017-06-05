from Helpers.AbstractService import AbstractService
from Services.Phonebook.PhonebookContents import PhonebookContents


class Phonebook(AbstractService):
    def addEndpoints(self):
        self.addUrl('phonebook', PhonebookContents)
