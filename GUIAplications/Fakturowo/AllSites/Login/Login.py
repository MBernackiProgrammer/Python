import this
import PySimpleGUI as sg

class Login:
    def IDErrorSubsystemLogin():
        print("Error")

    def EMailErrorSubsystemLogin():
        print("Error")

    def IDLoginSubsystem(ID, Passworld):
        print("Your login :")
        print(ID)
        print("Your password")
        print(Passworld)

    def LoginSite():
        Layout = [
            [sg.Text("Something")],
            [sg.Text("Login by: ")],
            [sg.Button("Workers ID")],
            [sg.Button("Workers E-Mail")]
        ]

        window = sg.Window('File Compare', Layout, size = (750,400))
        while True:                             # The Event Loop
            event, values = window.read()
            # print(event, values) #debug
            if event in (None, 'Exit', 'Cancel'):
                break

            if event == 'Workers ID':
                Login.LoginByID()
                window.close()

            if event == 'Workers E-Mail':
                Login.LoginByEMail()
                window.close()

    def LoginByID():
        print("Login by ID")
        Layout = [
            [sg.Text("Something")],
            [sg.Text("Your ID :")],
            [sg.InputText("")],
            [sg.Text("Your password")],
            [sg.InputText("")],
            [sg.Button("Return"), sg.Button("Login")]
        ]

        window = sg.Window('File Compare', Layout, size = (750,400))
        while True:                             # The Event Loop
            event, values = window.read()
                # print(event, values) #debug
            if event in (None, 'Exit', 'Cancel'):
                break
            if event == 'Return':
                Login.LoginSite()
                window.close()
        
            if event == 'Login':
                Login.IDLoginSubsystem()
                window.close()


    def LoginByEMail():
        print("Login by e - mail")
        Layout = [
            [sg.Text("Something")],
            [sg.Text("Login by: ")],
            [sg.Button("Workers ID")],
            [sg.Button("Workers E-Mail")]
        ]

        window = sg.Window('File Compare', Layout, size = (750,400))
        while True:                             # The Event Loop
            event, values = window.read()
    # print(event, values) #debug
            if event in (None, 'Exit', 'Cancel'):
                break










