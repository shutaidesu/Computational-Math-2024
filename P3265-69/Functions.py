import math

def F1(x):
    return x ** 3 - 3.125 * x ** 2 - 3.5 * x + 2.458

def DF1(x):
    return 3 * x ** 2 - 6.25 * x - 3.5

def DDF1(x):
    return 6 * x - 6.25

def F2(x):
    return 2 * x ** 3 - 1.89 * x ** 2 - 5 * x + 2.34

def DF2(x):
    return 6 * x ** 2 - 3.78 * x - 5

def DDF2(x):
    return 12 * x - 3.78

def F3(x):
    return math.exp(x) - 3

def DF3(x):
    return math.exp(x)

def DDF3(x):
    return math.exp(x)

def F4(x, y):
    return x ** 2 + y ** 2 - 4

def F5(x, y):
    return -3 * x ** 2 + y

def DF4_DX(x):
    return 2 * x

def DF4_DY(y):
    return 2 * y

def DF5_DX(x):
    return -6 * x

def DF5_DY():
    return 1
