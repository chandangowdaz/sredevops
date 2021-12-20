def myfunc(num1,num2):
    return (num1+num2) == 20 or num1==20 or num2 == 20
    #if num1 == 20 or num2 == 20:
        #return True
    #elif num1+num2 == 20:
        #return True
    #else:
        #return False

num1 = int(input("Enter the number 1 \n"))
num2 = int(input("Enter the number 2 \n"))

print(myfunc(num1,num2))