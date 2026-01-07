print("Hello")

def f(x):
    return x + 1

def g(x):
    return x * 2

def h(x,y):
    return x ** y

def i(x):
    return x ** 2 - x + 2

def j(x):
    if x < 0:
        return x * 2
    else:
        return x + 1


print(f(4))
print(g(4))
print(h(2,10))
print(i(3))
print(j(-1))