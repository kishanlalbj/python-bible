a = 128

def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

def f1():
    global a
    a = 300
    print(a)

def f2():
    a = 40
    print(a)


def about(name,age,likes,place="Rasipuram"):
    print("Meet {}! They are {} years old and they like {} and from {}".format(name,age,likes,place))

about("kishan",23,"Python")
about(age=24,likes="Java",name="Raj")

f1()
f2()
print(a)
print(add(10,10,34))