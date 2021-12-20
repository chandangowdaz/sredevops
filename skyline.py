def myfunc(name):
    l1 = []

    for i in range(len(name)):
        if i % 2 == 0:
            l1.append(name[i].upper())
        else:
            l1.append(name[i].lower())

    return ''.join(l1)

name = input("Enter you name\n")
print(myfunc(name))