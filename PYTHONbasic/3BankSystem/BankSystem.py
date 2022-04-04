#Not ready
UsersID = []
UsersPassworlds = []
UserMoney = []

def CreateAccount():
    print("create account")











def Menu():
    print("=== Menu ===")
    print("Select option")
    option = input("Write number from x to y ")

    match(option):
        case '1':
            return 0

        case '2':
            return 0

        case _: 
            print("Plese write oprtion from x to y")   
            Menu()    
            return 0

def LogIn():
    print("Write login and passworld")
    login = input("Login : ")
    login = input("Passworld : ")

print("Have you got account in our bank ?")
MenuOption = input("select Y / N ")



LogIn()
print("Welcome back, how can I help you ?")
while True:
    Menu()