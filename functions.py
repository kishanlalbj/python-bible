a = 128

def add(a,b):
    return a + b


def f1():
    global a
    a = 300
    print(a)

def f2():
    a = 40
    print(a)
    
f1()
f2()
print(a)