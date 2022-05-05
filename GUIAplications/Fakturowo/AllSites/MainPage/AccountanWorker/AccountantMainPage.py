import PySimpleGUI as sg

class MainPage:
    
    def SpawnMainPage(self):
        print("Error")
        Layout = [
            [sg.Text("Sorry, but we can't login you to your account")],
            [sg.Button("Main page")],
            [sg.Button("Income")],
            [sg.Button("Outins")],
            [sg.Button("Settings")]
        ]

        window = sg.Window('File Compare', Layout, size = (750,400))
        while True:                             
            event, values = window.read()
            if event in (None, 'Exit', 'Cancel'):
                break
