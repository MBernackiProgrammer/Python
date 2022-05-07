##########################################################
#
# Tasks for this source / zadania tego pliku
#   1. Login / Logowanie
#       a) Create "Login" object / storzenie obiektu "Login"
#       b) Spawn login site / utworzenie strony logowania
#   2. 
#   3. 
#
##########################################################
import PySimpleGUI as sg
from AllSites.Login.Login import*
from AllSites.MainPage.AccountanWorker.AccountantMainPage import*

class Worker:
    IsAdmin = bool(False)
    PositionIndex = int(-1)
    WorkerID = int(-1)
    WorkerEMain = "NONE"
    WorkerPassword = "NONE"
    WorkerName = "NONE"

LoginSite = Login()
LoginSite.LoginSite()

IndexOfPosition = int(1)
MainPageSite = AccountantMainPage()

while True:
    if LoginSite.loged == True:
    # 1 = accountant worker
    # 2 = Warehouse worker
        match IndexOfPosition:
            case 1:
                MainPageSite.SpawnMainPage(LoginSite.Login)
                break
                
    else: 
        print("Error")

