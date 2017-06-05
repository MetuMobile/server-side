from os import path


class Config:
    serverType = "Deployment"
    serverIp = "144.122.156.67"
    serverPort = 1071
    os = 'Linux'
    debug = True

    home = path.dirname(path.abspath(__file__))
    APP_DIR = home
    dynamicFilesFolderPath = path.join(home, 'dynamicFiles')

    # staticFolderPath = path.join(home, "imageUploads")
    # dynamicFolderPath = path.join(home, "dynamicImages")
    # loggerPath = path.join(home, 'log.txt')
    # cafeteriaMenuExcelPath = path.join(home, 'Cafeteria', 'cafeteriaMenu.xlsx')

    staticFolderPath = path.join(home, 'imageUploads')
    dynamicFolderPath = path.join(home, 'dynamicImages')
    loggerPath = 'log.txt'
    cafeteriaMenuExcelPath = path.join(home, 'Services', 'Cafeteria', 'Menus', 'cafeteriaMenu.xlsx')

    serverRootLink = "http://" + serverIp + ":" + str(serverPort) + "/api/v1"
    servicesLink = serverRootLink + "/"
