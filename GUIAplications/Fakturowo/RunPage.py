import PySimpleGUI as sg
from AllSites.Login.Login import*
from AllSites.MainPage.AccountantMainPage import*

LoginSite = Login()
LoginSite.LoginSite()

if LoginSite.loged == True:
    IndexOfPosition = int(1)
    MainPageSite = MainPage()   
    # 1 = accountant worker
    # 2 = Warehouse worker
    match IndexOfPosition:
        case 1:
            MainPageSite.SpawnMainPage()

        case 2:
            MainPageSite.SpawnMainPage()

    
else:
    print("Error")

