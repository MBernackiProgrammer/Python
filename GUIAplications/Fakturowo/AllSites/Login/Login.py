import PySimpleGUI as sg

class Login:
    def IDErrorSubsystemLogin():
        print("Error")
        Layout = [
            [sg.Text("Sorry, but we can't login you to your account")],
            [sg.Button("Try again"), sg.Button("Select another option of logining")]
        ]

        window = sg.Window('File Compare', Layout, size = (750,400))
        while True:                             
            event, values = window.read()
            if event in (None, 'Exit', 'Cancel'):
                break

            if event == 'Try again':
                Login.LoginByID()
                window.close()

            if event == 'Select another option of logining':
                Login.LoginSite()
                window.close()

    def EMailErrorSubsystemLogin():
        print("Error")

    def IDLoginSubsystem(ID, Passworld):
        print("Your login :")
        print(ID)
        print("Your password")
        print(Passworld)
        if(ID == "1234" and Passworld == "1234"):
            print("Launch program")
        else:
            Login.IDErrorSubsystemLogin()

    def LoginSite():
        Layout = [
            [sg.Text("Login by: ")],
            [sg.Button("Workers ID")],
            [sg.Button("Workers E-Mail")]
        ]

        window = sg.Window('File Compare', Layout, size = (750,400))
        while True:
            event, values = window.read()
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
        while True:
            event, values = window.read()
            if event in (None, 'Exit', 'Cancel'):
                break
            if event == 'Return':
                Login.LoginSite()
                window.close()
        
            if event == 'Login':
                Login.IDLoginSubsystem(values[0], values[1])
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
        while True:
            event, values = window.read()
            if event in (None, 'Exit', 'Cancel'):
                break