def uloha1(s):
    a = s.count("a")
    return a


def is_palindrome(s):
    return s == s[::-1]


def rotate_word(s, n):
    n = n % 26
    s_end = ""
    for k in s:
        b = ord(k)
        if k.islower():
            if b + n > 122:
                s_end += chr(b + n - 26)
            elif b + n < 97:
                s_end += chr(b + n + 26)
            else:
                s_end += chr(b + n)
        else:
            if b + n > 90:
                s_end += chr(b + n - 26)
            elif b + n < 60:
                s_end += chr(b + n + 26)
            else:
                s_end += chr(b + n)
    return s_end


def has_no_e(s):
    if "e" in s.lower():
        return False
    else:
        return True


def word_reader():
    file = open("word.txt", "r")
    a = file.readline() + " "
    word_count = 0
    current_word = ""
    e_words = 0
    for c in a:
        if c == " ":
            word_count += 1
            if not has_no_e(current_word):
                print(current_word)
                e_words += 1
            current_word = ""
        else:
            current_word += c
    return f"{(e_words/word_count)*100}%"


def avoids(s, f):
    for b in f:
        if b in s:
            return False
    return True


def avoids_words():
    file = open("word.txt", "r")
    a = file.readline() + " "
    current_word = ""
    forbidden = input()
    for c in a:
        if c == " ":
            if avoids(current_word, forbidden):
                print(current_word)
            current_word = ""
        else:
            current_word += c
    return


def uses_only(s, o):
    for b in o:
        if b not in s:
            return False
    return True


def uses_all(s, o):
    a = 1
    for b in o:
        a = a * b in s
    return a


def is_abecederian(s):
    s = s.lower()
    n = len(s)
    for i in range(n-1):
        if not ord(s[i]) <= ord(s[i+1]):
            return False
    return True


def double_con(s):
    s = s.lower()
    n = len(s)
    a = 0
    b = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            a += 1
            b = 1
        elif b == 1:
            b = 0
        else:
            a = 0
        if a == 3:
            return True
    return False


def palindromic():
    for i in range(100000, 999999):
        s = str(i)
        s1 = s[0:5]
        s2 = s[1:6]
        s3 = s[0:4]
        s4 = s[1:5]
        s5 = s[2:6]
        if s == s[::-1]:
            if s1 == s1[::-1]:
                if s2 == s2[::-1]:
                    if s3 == s3[::-1]:
                        if s4 == s4[::-1]:
                            if s5 == s5[::-1]:
                                print(s)
    return


def mom_and_son(d):
    for i in range(100-d):
        if str(i).zfill(2) == str(d+i)[::-1]:
            print(f"{i} a {d+i}")
    return
