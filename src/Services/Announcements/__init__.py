from Helpers.AbstractService import AbstractService
from Services.Announcements.Root import Root


class Announcements(AbstractService):
    def __init__(self):
        super().__init__()

        rootView = Root.as_view('root')
        self.blueprint.add_url_rule('/', view_func=rootView, methods=['GET', ])

