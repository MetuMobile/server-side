from Helpers.AbstractService import AbstractService
from Services.Shuttle.Location import Location
from Services.Shuttle.Root import Root
from Services.Shuttle.Schedule import Schedule


class Shuttle(AbstractService):
    def __init__(self):
        super().__init__()

        ScheduleView = Schedule.as_view('schedule')
        self.blueprint.add_url_rule('/schedule/', view_func=ScheduleView)

        LocationView = Location.as_view('location')
        self.blueprint.add_url_rule('/location/', view_func=LocationView)

        rootView = Root.as_view('root')
        self.blueprint.add_url_rule('/', defaults={'serviceName': self.serviceName}, view_func=rootView)

