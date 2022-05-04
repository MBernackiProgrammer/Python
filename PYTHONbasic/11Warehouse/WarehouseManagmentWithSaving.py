
class Product:
    #variables - user data
    UserName = ""
    UserSave = ""
    #variables - product data 

    #def to menu 
    def StartMenu():
        while True:
            print("Select option :")
            print("1. Last session.")
            print("2. New session.")
            OptionSelected = int()
            OptionSelected = input("from 1 to 2")
            if(OptionSelected > 0 and OptionSelected < 2):
                break      

        match(OptionSelected):
            case 1:
                print("Write save name :")

                return 0
            case 2:
                print("Write your name :")
                UserName = input()
                print("Save name :")
                UserSave = input()
                return 0
    
    def InMenu():
        print("Select option :")
        print("1. Show all produkts ")
        print("2. Add produkts")
        print("3. Search for a product")

    #def to managment data

string = str("1234")
interger = int(1234)
floatcos = float(12.34)

klasa = Product


