import PySimpleGUI as sg
from AllSites.Login.Login import*
from AllSites.MainPage.AccountanWorker.AccountantMainPage import*

LoginSite = Login()
LoginSite.LoginSite()

IndexOfPosition = int(1)
MainPageSite = AccountantMainPage()

if LoginSite.loged == True:
    # 1 = accountant worker
    # 2 = Warehouse worker
    match IndexOfPosition:
        case 1:
            MainPageSite.SpawnMainPage(LoginSite.Login)

    
else:
    print("Error")

