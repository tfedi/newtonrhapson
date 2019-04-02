def sum(a,b):
    return a+b

def substraction(a,b):
    return a-b

def division(a,b):
    if(b!=0):
        return a/b
    else:
        return False

def product(a,b):
    return a*b


def showMenu():
    print("1) Sum \n")
    print("2) Substraction \n")
    print("3) Division \n")
    print("4) Product \n")
    print("5) Exit \n")

flag = 0;

while(flag==0):
    showMenu()
    numA = int(input("Select NUM A : \n"))
    numB = int(input("Select NUM B: \n"))
    option = int(input("Select an option below: \n"))
    
    if(option == 1):
        print(sum(numA,numB))
    elif(option == 2):
        print(substraction(numA,numB))
    elif(option == 3):
        print(division(numA,numB))
    elif(option == 4):
        print(product(numA,numB))
    elif(option == 5):
        break
