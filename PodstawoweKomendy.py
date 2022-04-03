#zmienna w pythonie / nie ma typów 
wartosc = 1234

#Funckja bez argumentów 
def FunkcjaBezArgumentow():
    print("Test2")

#Wywoływanie funcji 
FunkcjaBezArgumentow()

#Funcja z argumentem 
def FunkcjaZArgumentem(x):
    print(x)

#Wywoływanie funkcji 
FunkcjaZArgumentem(5)

#Swich in python, a nie jednak tu się nazywa match
variable = 1


def f(x):
    match x:
        case 'a':
            return 1
        case 'b':
            return 2
        case _:        
            return 0   # 0 is the default case if x is not found

print(f('a'))


