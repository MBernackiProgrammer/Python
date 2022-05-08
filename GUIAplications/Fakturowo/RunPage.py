##########################################################
#
# Tasks for this source / zadania tego pliku
#   1. Create worker class / stworzenie klasy robotniczej 
#   2. Login / Logowanie
#       a) Create "Login" object / storzenie obiektu "Login"
#       b) Spawn login site / utworzenie strony logowania
#   3. Create worker object, named "WorkerData" / stworzenie obiektu worker o nazwie "WorkerData"
#   4.
#   5.  
#
##########################################################
import PySimpleGUI as sg
from AllSites.Login.Login import*
from AllSites.MainPage.AccountanWorker.AccountantMainPage import*
from AllSites.MainPage.MainPageManager import*

#AD1
class Worker:
    IsAdmin = bool(False)
    PositionIndex = int(-1)
    WorkerID = int(-1)
    WorkerEMain = "NONE"
    WorkerPassword = "NONE"
    WorkerName = "NONE"

#AD2
LoginSite = Login()
LoginSite.LoginSite()

#AD3
WorkerData = Worker()

#AD4
MainPageSite = AccountantMainPage()
MainPageManagerSite = MainPageManager()

#AD5
while True:
    if LoginSite.loged == True:
        MainPageManagerSite.ChechPosition(WorkerData)
        break
                
    else: 
        print("Error")

