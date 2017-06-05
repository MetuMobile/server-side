from Helpers.AbstractService import AbstractService
from Services.Cafeteria.MealImportExcelFileRefresh import MealImportExcelFileRefresh
from Services.Cafeteria.Meals import Meals
from Services.Cafeteria.WebMenuUploader import WebMenuUploader, WebMenuUploadComplete


class Cafeteria(AbstractService):
    def addEndpoints(self):
        self.addUrl('meals', Meals)
        self.addUrl('readExcelImport', MealImportExcelFileRefresh)
        self.addUrl('excelUpload', WebMenuUploader, 'upload')
        self.addUrl('excelUploadComplete', WebMenuUploadComplete, 'complete')
        # self.addUrl('', )
        pass

