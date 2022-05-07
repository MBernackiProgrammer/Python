##########################################################
#
# Tasks for this source / zadania tego pliku
#   1.
#   2.
#   3.
#   4.
#   5.
#
##########################################################
import PySimpleGUI as sg

class Login:
    loged = bool(False)
    Password = ""
    Login = ""

# Main page og logging/ stona glowna logowania
    def LoginSite(self):
        Layout = [
            [sg.Text("Login by: ")],
            [sg.Button("Workers ID")],
            [sg.Button("Workers E-Mail")]
        ]

        window = sg.Window('Fakturowo', Layout, size = (750,400))
        while True:
            event, values = window.read()
            if event in (None, 'Exit', 'Cancel'):
                break

            if event == 'Workers ID':
                Login.LoginByID(self)
                window.close()

            if event == 'Workers E-Mail':
                Login.LoginByEMail(self)
                window.close()

    #Login by company ID
    def LoginByID(self):
        print("Login by ID")
        Layout = [
            [sg.Text("Your ID :") ],
            [sg.InputText("", justification='center')],
            [sg.Text("Your password")],
            [sg.InputText("", justification='center')],
            [sg.Button("Return"), sg.Button("Login")]
        ]

        window = sg.Window('Fakturowo', Layout, size = (750,400))
        while True:
            event, values = window.read()
            if event in (None, 'Exit', 'Cancel'):
                break
            if event == 'Return':
                Login.LoginSite(self)
                window.close()
        
            if event == 'Login':
                Login.IDLoginSubsystem(self ,values[0], values[1])
                window.close()

    #Login by business e-mail
    def LoginByEMail(self):
        print("Login by e - mail")
        Layout = [
            [sg.Text("Something")],
            [sg.Text("Login by: ")],
            [sg.Button("Workers ID")],
            [sg.Button("Workers E-Mail")]
        ]

        window = sg.Window('Fakturowo', Layout, size = (750,400))
        while True:
            event, values = window.read()
            if event in (None, 'Exit', 'Cancel'):
                break

# Login to FOS / logowanie do FOS

    def IDLoginSubsystem(self,ID, Passworld):
        if(ID == "1234" and Passworld == "1234"):
            Login.Password = Passworld
            Login.Login = ID
            self.loged = bool(True)
            print("Launch program")
        else:
            Login.IDErrorSubsystemLogin(self)

# Errors messages / wiadomosci o blendach
    #Logging by ID errors / błędy logowania przez ID
    def IDErrorSubsystemLogin(self):
        print("Error")
        Layout = [
            #error content / treść błędu 
            [sg.Text("Sorry, but we can't login you to your account")],
            #options to select / opcje do wyboru 
            [sg.Button("Try again"), sg.Button("Select another option of logining")]
        ]

        window = sg.Window('Fakturowo', Layout, size = (750,400))
        while True:                             
            event, values = window.read()
            if event in (None, 'Exit', 'Cancel'):
                break
            
            #If press "Try again" button / jeśli użytkownik naciśnie przycisk "Try again"
            if event == 'Try again':
                Login.LoginByID(self)
                window.close()

            #If press "Select another option of logining" button / jeśli użytkownik naciśnie przycisk "Select another option of logining"
            if event == 'Select another option of logining':
                Login.LoginSite(self)
                window.close()

    #Logging by E - Mail errors / błędy logowania przez e-mail
    def EMailErrorSubsystemLogin(self):
        print("Error")