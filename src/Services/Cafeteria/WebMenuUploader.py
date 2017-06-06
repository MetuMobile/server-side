from flask import render_template, request
from datetime import datetime
import os
from Config import Config
from flask.views import MethodView

from Helpers.Admin import Admin
from Services.Cafeteria import MealImportExcelFileRefresh


class WebMenuUploader(MethodView):
    def get(self):
        Admin().checkSuperAdminAuth()
        return render_template("upload.html")

class WebMenuUploadComplete(MethodView):
    def post(self):
        targetFolder = os.path.join(Config.excelExportFilesFolderPath)
        if not os.path.isdir(targetFolder):
            os.mkdir(targetFolder)

        selected_files = request.files.getlist("file")
        time_stamp = str(datetime.now().timestamp())
        for file in selected_files:
            file_name = time_stamp+'.xlsx'
            destination = os.path.join(Config.excelExportFilesFolderPath, file_name)# "/".join([target, file_name])
            file.save(destination)
            MealImportExcelFileRefresh(destination).updateCafeteriaMenu() # patlarsa buradan patliyor olabilir.
            # unresolved reference olacak cunku

        return render_template("complete.html")
