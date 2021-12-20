def myfunc(text):
    mylist = text.split()
    return mylist[0][0].lower() == mylist[1][0].lower()


print(myfunc('Abrab affpj'))