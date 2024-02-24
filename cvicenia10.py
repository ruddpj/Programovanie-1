from random import randint


def uloha1():
    a = int(input())
    zoz = []
    while a != 0:
        zoz.append(a)
        a = int(input())
    return max(zoz)


def chop(zoz):
    if len(zoz) > 1:
        zoz.pop(0)
        zoz.pop(-1)
    else:
        zoz = []
    return zoz


def uloha3(m, n):
    a = len(m)
    b = len(m[0])
    if a == len(n) and b == len(n[0]):
        for i in range(a):
            for j in range(b):
                m[i][j] += n[i][j]
        return m
    else:
        return "Matice nie je schopné sčítať"


def uloha4(m, n):
    zoz = []
    if len(m[0]) == len(n):
        for i in range(len(m)):
            zoz.append([])
            for j in range(len(n[0])):
                a = 0
                for k in range(len(m)):
                    a += m[i][k]*n[k][j]
                zoz[i].append(a)
        return zoz
    else:
        return "Matice nie je schopné vynásobiť"


def uloha5(t):
    zoz = t[0]
    for i in range(len(t)-1):
        if zoz[0] < t[i+1][0]:
            zoz[0] = t[i+1][0]
        if zoz[1] > t[i+1][1]:
            zoz[1] = t[i+1][1]

    if zoz[0] < zoz[1]:
        return True
    else:
        return False


def has_duplicates(t):
    for i in range(len(t)):
        a = 0
        for j in range(len(t)):
            if t[i] == t[j]:
                a += 1
            if a > 1:
                return True
    return False


def birthday():
    t = []
    for i in range(23):
        t.append(randint(1, 366))

    return has_duplicates(t)


def words():
    zoz = []
    file = open("word.txt", "r")
    t = file.readline().strip()
    w = ""
    for i in range(len(t)):
        if t[i] == " ":
            zoz = zoz + [w]
            w = ""
        else:
            w += t[i]
    return zoz


def in_bisect(w, t):
    while len(t) > 0:
        a = int(round(len(t)/2))
        s = t[a]
        if s == w:
            return True
        elif w > s:
            t = t[a+1:]
        else:
            t = t[:a]
    return False


def reverse_pair(a, b):
    if a == b[::-1]:
        return True
    return False


def interlock(a, b, c):
    w = ""
    if len(a) == len(b) == len(c):
        for i in range(len(a)):
            w += a[i] + b[i] + c[i]
        return w
    return False


def uloha7(t):
    zoz = []
    for i in range(len(t)):
        a = t[i]
        n = 2
        if a == 1:
            zoz.append(1)

        while n <= a:
            if a % n == 0:
                zoz.append(n)
                a = a / n
            else:
                n += 1
        zoz.append(0)
    return zoz


def uloha8(t):
    zoz = []
    for i in range(0, len(t), 3):
        if t[i] < t[i+1]:
            if t[i] < t[i+2]:
                zoz.append(t[i])
                zoz.append(t[i+1])
                zoz.append(t[i+2])
            else:
                zoz.append(t[i+2])
                zoz.append(t[i])
                zoz.append(t[i+1])
        elif t[i+1] < t[i+2]:
            zoz.append(t[i+1])
            if t[i] < t[i+2]:
                zoz.append(t[i])
                zoz.append(t[i+2])
            else:
                zoz.append(t[i+2])
                zoz.append(t[i])
        else:
            zoz.append(t[i+2])
            zoz.append(t[i+1])
            zoz.append(t[i])
    return zoz


def uloha8b(t):
    for i in range(0, len(t), 3):
        if t[i] < t[i+1]:
            if t[i] < t[i+2]:
                t[i], t[i+1], t[i+2] = t[i], t[i+1], t[i+2]
            else:
                t[i], t[i+1], t[i+2] = t[i+2], t[i], t[i+1]
        elif t[i+1] < t[i+2]:
            if t[i] < t[i+2]:
                t[i], t[i+1], t[i+2] = t[i+1], t[i], t[i+2]
            else:
                t[i], t[i+1], t[i+2] = t[i+1], t[i+2], t[i]
        else:
            t[i], t[i + 1], t[i + 2] = t[i+2], t[i+1], t[i]
    return t
