
class Product:
    #variables - user data
    
    UserName = ""
    UserSave = ""
    
    #variables - product data 

    def SearchForProduct():
        #Search for product
        print()
        Product.InMenu()

    def AddProduckt():
        #Add product
        print("")
        Product.InMenu()

    def ShowAllProducts():
        #Print all produts
        print("")
        Product.InMenu()

    #def to menu 
    def StartMenu():  
        print("Your name")
        Product.UserName = input()    
    
    #Function print menu in aplication 
    def InMenu():
        SelectedOption = ""
        while True:
            print("Select option :")
            print("1. Show all produkts ")
            print("2. Add produkts")
            print("3. Search for a product")
            SelectedOption = input()
            if(SelectedOption != ""):
                SelectedOption = int(SelectedOption)
                if(SelectedOption > 0 and SelectedOption <= 3):
                    break
                
            else:
                print("Try again correct range is from 1 to 3")

            

        match(SelectedOption):
            case 1:
                Product.ShowAllProducts()
                return 0
            
            case 2: 
                Product.AddProduckt()
                return 0

            case 3:
                Product.SearchForProduct()
                return 0
            
    #def to managment data
string = str("1234")
interger = int(1234)
floatcos = float(12.34)

klasa = Product
klasa.InMenu()



