# import turtle as tutel


def uloha1(n):
    if n > 0:
        return n + uloha1(n-1)
    else:
        return 0


def uloha2(n):
    if n > 0:
        a = int(input())
        return a + uloha2(n - 1)
    else:
        return 0


def uloha3(n):
    if n > 0:
        a = int(input())
        if a % 2 == 0:
            b = 1
        else:
            b = 0
        return b + uloha3(n - 1)
    else:
        return 0


def uloha4(n, max_a):
    if n > 0:
        a = int(input())
        if a > max_a:
            max_a = a
        return uloha4(n-1, max_a)
    else:
        return max_a


def uloha5(n):
    if n > 0:
        a = int(input())
        b = a % 2
        c = uloha5(n-1)
        if b == c:
            return True
        else:
            return False
    else:
        return 0


def uloha6(n):
    if n > 1:
        for i in range(2, n):
            if not n % i:
                return uloha6(n-1)
        print(n)
        return n + uloha6(n-1)
    else:
        return 0


def is_palindrome(m, n):    # uloha 8
    if len(m)/2 > n:
        if not m[n] == m[(-1*n)-1]:
            return False
        return is_palindrome(m, n+1)
    return True


def is_power(n, x, i):      # uloha 9
    if n >= x**i:
        if n == x**i:
            return True
        return is_power(n, x, i+1)
    return False


def gcd(n, m):      # uloha 10
    if n < m:
        n, m = m, n
    if n != m:
        n = n-m
        return gcd(n, m)
    return n


def draw(t, length, n):     # uloha 11
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


def koch(t, length, ang, n):
    if n > 0:
        draw(t, length, 3)
        if ang == 60:
            t.left(60)
            ang = 120
        else:
            t.right(120)
            ang = 60
        koch(t, length, ang, n-1)
    return


def uloha12(n):
    if n > 0:
        a = str(n % 2)
        return uloha12(n//2) + a
    return "0"


def uloha13(n, p, lst):
    if p > 0:
        if not n % 0.5:
            lst.append("0.5€")
            return uloha13(n-0.5, p - 1, lst)
        elif not n % 0.2:
            lst.append("0.2€")
            return uloha13(n - 0.2, p - 1, lst)
        elif not n % 0.1:
            lst.append("0.1€")
            return uloha13(n - 0.1, p - 1, lst)
        elif not n % 0.05:
            lst.append("0.05€")
            return uloha13(n - 0.05, p - 1, lst)
        elif not n % 0.02:
            lst.append("0.02€")
            return uloha13(n - 0.02, p - 1, lst)
        else:
            lst.append("0.01€")
            return uloha13(n - 0.01, p - 1, lst)
    if p == 0 and n == 0:
        return f"True, {lst}"
    return False
