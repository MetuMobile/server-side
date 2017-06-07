from Helpers.AbstractService import AbstractService
from Services.Booklet.Root import Root


class Booklet(AbstractService):
    def __init__(self):
        super().__init__()

        rootView = Root.as_view('root')
        self.blueprint.add_url_rule('/<int:bookletId>',
                                    view_func=rootView, methods=['GET', ])
        self.blueprint.add_url_rule('/', defaults={'bookletId': None},
                                    view_func=rootView, methods=['GET', ])
