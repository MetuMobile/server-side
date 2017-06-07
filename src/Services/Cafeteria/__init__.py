from Helpers.AbstractService import AbstractService
from Services.Cafeteria.MealImportExcelFileRefresh import MealImportExcelFileRefresh
from Services.Cafeteria.Meals import Meals
from Services.Cafeteria.Root import Root
from Services.Cafeteria.WebMenuUploader import WebMenuUploader, WebMenuUploadComplete


class Cafeteria(AbstractService):

    def __init__(self):
        super().__init__()

        mealsView = Meals.as_view('meals')
        self.blueprint.add_url_rule('/meals/<mealId>', view_func=mealsView)
        self.blueprint.add_url_rule('/meals/', defaults={'mealId': None}, view_func=mealsView)

        mealImportExcelFileRefreshView = MealImportExcelFileRefresh.as_view('mealImportExcelFileRefresh')
        self.blueprint.add_url_rule('/readExcelImport', view_func=mealImportExcelFileRefreshView)

        WebMenuUploaderView = WebMenuUploader.as_view('WebMenuUploader')
        self.blueprint.add_url_rule('/excelUpload', view_func=WebMenuUploaderView)

        WebMenuUploadCompleteView = WebMenuUploadComplete.as_view('WebMenuUploadComplete')
        self.blueprint.add_url_rule('/excelUploadComplete', view_func=WebMenuUploadCompleteView)

        rootView = Root.as_view('root')
        self.blueprint.add_url_rule('/', view_func=rootView)
