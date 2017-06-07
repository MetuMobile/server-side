from Helpers.AbstractService import AbstractService
from Services.Event.Root import Root
from Services.Event.Upcoming import Upcoming
from Services.Event.UpcomingRaw import UpcomingRaw


class Event(AbstractService):
    def __init__(self):
        super().__init__()

        UpcomingView = Upcoming.as_view('upcoming')
        self.blueprint.add_url_rule('/upcoming/', view_func=UpcomingView)

        rootView = Root.as_view('root')
        self.blueprint.add_url_rule('/', view_func=rootView)
