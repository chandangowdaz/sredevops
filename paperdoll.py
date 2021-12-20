def myfunc(text):
    l1 = []
    for i in text:
        l1.append(i*3)
    return "".join(l1)

print(myfunc('Hello'))
#myfunc('abc')