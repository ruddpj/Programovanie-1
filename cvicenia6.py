import math


def uloha1():
    x = int(input())
    a = 0
    while x > 0:
        a += x
        x = int(input())
    return a


def uloha2(n):
    x = 0
    a = range(0, n)
    while x < n:
        if x**(1/2) in a:
            print(x)
        x += 1
    return


def uloha3(n):
    x = 0
    while 2**x < n:
        x += 1
    return x-1


def uloha4():
    x = int(input())
    a = x
    b = 1
    b_max = 1
    while x != 0:
        x = int(input())
        b += 1
        if x > a:
            a = x
            b_max = b
    return b_max


def uloha5():
    x = int(input())
    b = 0
    while x != 0:
        a = int(input())
        if x < a:
            b += 1
        x = a
    return b


def uloha6():
    x = int(input())
    a = x
    b = 1
    while x != 0:
        x = int(input())
        if x == a:
            b += 1
        elif x > a:
            a = x
            b = 1
    return b


def uloha7():
    x = int(input())
    a = x
    b = 1
    b_max = 1
    while x != 0:
        x = int(input())
        if x == a:
            b += 1
        else:
            b = 0
        if b > b_max:
            b_max = b
    return b_max


def uloha8(n):
    x = 0
    a = 1
    b = 2
    if n == 0:
        return 1
    while x < n:
        x, a = a, a+x
        if x == n:
            return b
        b += 1
    return -1


def mysqrt(a):      # uloha9
    x = 2
    y = 0
    for i in range(100):
        y = (x+a/x)/2
        x = y
    return y


def test_square_root(n):
    print("a    mysqrt()    math.sqrt()     diff")
    for i in range(1, n+1):
        x = round(mysqrt(i), 5)
        y = round(math.sqrt(i), 5)
        d = round(abs(x-y), 5)
        print(f"{i}     {x: 8}       {y: 8}       {d: 8}")
    return


def eval_loop():        # uloha10
    while True:
        a = input()
        b = eval(a)
        print(b)


def estimate_pi():      # uloha11
    x = math.factorial(0)*(1103+0)/(math.factorial(0)**4)*(396**0)
    k = 1
    while x > 1e-15:
        a = math.factorial(4*k)*(1103+26390*k)/(math.factorial(k)**4)*(396**(4*k))
        x += a
        k += 1
    x = x*(math.sqrt(2)*2/9801)
    return 1/x


def kvocient(a, b):     # uloha12
    x = 0
    if a < b:
        return 0
    if b == 0:
        return None
    while a-b >= 0:
        a = a-b
        x += 1
    return x


def modulo(a, b):     # uloha13
    if a < b:
        return a
    if b == 0:
        return None
    while a-b >= 0:
        a = a-b
    return a


def faktorizacia(a):    # uloha14
    x = 2
    b = a
    while x <= a:
        if not b % x:
            print(x)
            b = b/x
        else:
            x += 1


print(faktorizacia(13))
