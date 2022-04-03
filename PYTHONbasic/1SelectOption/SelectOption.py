#Select option
#Wybierz opcję 

import datetime
def Menu(x):
    data = datetime.datetime.now()
    match x:
        case '1':
            return data.date()
        case '2':
            return data.time()
        case _:        
            return 0
            
print("Select option")
print("1. Show date")
print("2. Show hour")
option = input("")
print(Menu(option))