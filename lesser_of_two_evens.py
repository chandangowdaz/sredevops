def myfunc(num1,num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 > num2:
            return num2
        else:
            return num1
    elif num1 > num2:
        return num1
    else:
        return num2
    
num1 = int(input("Enter the first number \n"))
num2 = int(input("Enter the second number \n"))

print(myfunc(num1,num2))