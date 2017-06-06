from os import path


class Config:
    debug = True
    serverType = "Deployment"
    if debug==True:
        serverIp = "127.0.0.1"
    else:
        serverIp = "144.122.156.67"
    serverPort = 1071
    os = 'Linux'

    home = path.dirname(path.abspath(__file__))
    APP_DIR = home

    loggerPath = path.join(home, 'log.txt')
    excelExportFilesFolderPath = path.join(home, 'excelExportFiles')
    staticImageFolderPath = path.join(home, 'staticImages')
    resizedImagesFolderPath = path.join(home, 'resizedImages')
    cafeteriaMenuExcelPath = path.join(home, 'Services', 'Cafeteria', 'Menus', 'cafeteriaMenu.xlsx')

    serverRootLink = "http://" + serverIp + ":" + str(serverPort) + "/api/v1"
    servicesLink = serverRootLink + "/"
    cafeteriaServiceUrl = servicesLink + 'cafeteria'