from Helpers.AbstractService import AbstractService
from Services.Phonebook.PhonebookContents import PhonebookContents
from Services.Phonebook.Root import Root


class Phonebook(AbstractService):
    def __init__(self):
        super().__init__()

        PhonebookView = PhonebookContents.as_view('phonebook')
        self.blueprint.add_url_rule('/', defaults={'id': None}, view_func=PhonebookView)
        self.blueprint.add_url_rule('/<id>', view_func=PhonebookView)
