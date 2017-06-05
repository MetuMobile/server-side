from Helpers.AbstractService import AbstractService
from Services.Cafeteria.MealImportExcelFileRefresh import MealImportExcelFileRefresh
from Services.Cafeteria.Meals import Meals


class Cafeteria(AbstractService):
    def addEndpoints(self):
        self.addUrl('meals', Meals)
        self.addUrl('readExcelImport', MealImportExcelFileRefresh)
        # self.addUrl('excelUpload', )
        # self.addUrl('excelUploadComplete', )
        pass

