from Helpers.AbstractService import AbstractService
from Services.FeaturedApps.Android import Android
from Services.FeaturedApps.Ios import Ios
from Services.FeaturedApps.Root import Root
from Services.FeaturedApps.Windows import Windows


class FeaturedApps(AbstractService):
    def __init__(self):
        super().__init__()

        AndroidView = Android.as_view('android')
        self.blueprint.add_url_rule('/android/', view_func=AndroidView)

        IosView = Ios.as_view('ios')
        self.blueprint.add_url_rule('/ios/', view_func=IosView)

        WindowsView = Windows.as_view('windows')
        self.blueprint.add_url_rule('/windows/', view_func=WindowsView)
    
        rootView = Root.as_view('root')
        self.blueprint.add_url_rule('/', defaults={'serviceName': self.serviceName}, view_func=rootView)
