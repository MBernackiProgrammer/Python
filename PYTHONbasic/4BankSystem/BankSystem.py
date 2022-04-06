#Not ready
UsersID = []
UsersPassworlds = []
UserMoney = []

def CreateAccount():
    print("")
    IDuser = input("Your ID :")
    PassworldUser = input("Your passworld")
    return IDuser, PassworldUser

def Menu():
    print("=== Menu ===")
    print("Select option")

    print("1. Make a transfer")
    print("2. Rent monay")
    print("3. Change passworld")

    option = input("Write number from x to y ")

    match(option):
        case '1':
            return 0

        case '2':
            return 0
        
        case '3':
            return 0

        case _: 
            print("Plese write oprtion from x to y")   
            Menu()    
            return 0

def ErrorWithLogin():
    print("You made a mistake, try again...")
    id = input("User ID = ")
    passworld = input("Passworld = ")

def Login():
    while True:
        print("Ok, fine. Now please write your Bank ID :")
        WroteUserID = input("ID = ")
        print("and now passworld :")
        UserPassworld = input("Passworld = ")

        

        UserNameC = False
        UserPassworldC = False
        indexC = 0

        for x in UsersID:
            indexC = indexC + 1
            if x == WroteUserID:
                UserNameC = True
                break

        if len(UsersID) < 0:
            if UsersPassworlds[indexC] == UserPassworld:
                UserPassworldC = True
        
            if UserPassworldC and UserNameC == True:
                print("LogedIn")
        
            if UserPassworldC or UserNameC == False:
                print("Error try again")
                Login()
        else:
            print("Sorry, but we can't find your account, try again later")
            break
def Start():
    while True:
        print("Have you got account in our bank ?")
        MenuOption = input("select Y / N ")
        if MenuOption == 'Y':
            Login()
            break
        elif(MenuOption == "N"):
            print("Ok, bye")
            break
        elif(MenuOption!= "N" and MenuOption == "Y"):
            Start()

Start()
