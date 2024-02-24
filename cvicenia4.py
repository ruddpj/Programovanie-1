import turtle as tutel


def vypis(out):
    print(out)
    return


def test_parity(n):
    a = n % 2
    if a:
        vypis(a)
    else:
        vypis(a)
    return


def minimum_dvoch(a, b):
    if a < b:
        vypis(a)
    else:
        vypis(b)
    return


def minimum_troch(a, b, c):
    if a < b:
        if a < c:
            print(a)
        else:
            print(c)
    elif b < c:
        print(b)
    else:
        print(c)
    return


def menu():
    a = input()
    if a == "s":
        for i in range(4):
            tutel.forward(50)
            tutel.left(90)
    elif a == "t":
        for i in range(3):
            tutel.forward(50)
            tutel.left(120)
    else:
        print("dement")


def pocet_rovnakych(a, b, c):
    if a == b:
        if b == c:
            return 3
        else:
            return 2
    elif b == c or a == c:
        return 2
    else:
        return 0


def vstup1(n):
    num = 0
    for i in range(n):
        a = int(input())
        if not a % 5:
            num += 1
    return num


def vstup2(n):
    num = 0
    for i in range(n):
        a = int(input())
        num += a
    return num


def vstup3(n):
    a = int(input())
    num = a
    for i in range(n-1):
        a = int(input())
        if a < num:
            num = a
    return num


def vstup4(n):
    if n >= 2:
        a = int(input())
        num = a
        a = int(input())
        num2 = a
    else:
        a = int(input())
        return a
    if num < num2:
        num, num2 = num2, num
    for i in range(n-2):
        a = int(input())
        if num2 < a < num:
            num2 = a
        elif a > num:
            num, num2 = a, num
    return num2


def delitelnost(a, d):
    t = a % d
    return not t


def delitelnost_12():
    print(1)
    for i in range(2, 12):
        if delitelnost(12, i):
            print(i)
    print(12)


def test_prvociselnosti(n):
    if n == 2:
        return True
    for i in range(2, n):
        if delitelnost(n, i):
            return False
    return True


def test_prvociselnosti_50():
    for i in range(3, 50):
        if test_prvociselnosti(i):
            print(i)
    return


def pohyb_veze(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return True
    return False


def rovnaka_farba(x1, y1, x2, y2):
    if (x1 % 2 + y1 % 2) % 2 == (x2 % 2 + y2 % 2) % 2:
        return True
    return False


def pohyb_krala(x1, y1, x2, y2):
    if abs(x2-x1) in (0, 1) and abs(y2-y1) in (0, 1):
        return True
    return False


def pohyb_strelca(x1, y1, x2, y2):
    if abs(x1-x2) == abs(y1-y2):
        return True
    return False


def pohyb_damy(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
        return True
    return False


def pohyb_jazdca(x1, y1, x2, y2):
    if (abs(x2-x1) == 2 and abs(y2-y1) == 1) or (abs(x2-x1) == 1 and abs(y2-y1) == 2):
        return True
    return False
