import PySimpleGUI as sg

class AccountantMainPage:
    
    def SpawnMainPage(self, login):
        Welcome = "Welcome back " + login
        Layout = [
            [sg.Text(Welcome)],
            [sg.Button("Main page", size=(15,1))],
            [sg.Button("Income", size=(15,1))],
            [sg.Button("Outins", size=(15,1))],
            [sg.Button("Settings", size=(15,1))]
        ]

        window = sg.Window('Fakturowo', Layout, size = (750,400))
        while True:                             
            event, values = window.read()
            if event in (None, 'Exit', 'Cancel'):
                break
