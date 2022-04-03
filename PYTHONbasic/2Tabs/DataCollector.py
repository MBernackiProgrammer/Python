#Some tabs 
#Trochę tablic 

name = []
age = []
country = []

id = 0

def GetData():
    name.append(input("Your name : ")) 
    age.append(input("Your age : "))
    country.append(input("Your country : "))

def WhileHelper():
    while True:
        GetData()
        print("Would you print all data")
        UserInfo = input("Y / N your answer ")
        index = 0
        if UserInfo == "Y":
            while True:
                print("User number", index + 1,  "name is",  name[index],".")
                print("User number", index + 1, "is", age[index], "years old.")
                print("User number", index + 1, "live in", country[index], ".")
                if len(name) > index:
                    break
        print("Ok, maybe more datas ?")
        UserInfo = input("Y / N your answer ")
        if UserInfo == "N":
            print("Thanks, bye")
            break


print("Hi, I'm data collector, can you give me some datas?")
answer = input("Y / N your answer ")
if answer == "Y":
    WhileHelper()

if answer == "N":
    while True:
        print("You should say yes")
        answer2 = input("Y / N your answer ")
        if answer2 == "Y":
            break
    print("Ok, thanks now we can...")
    print("And now give me : ")
    WhileHelper()
        
            
        



    