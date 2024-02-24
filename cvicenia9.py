def nested_sum(zoz):
    sum_l = 0
    for elem in zoz:
        for num in elem:
            sum_l += num
    return sum_l


def cumsum(zoz):
    cum_zoz = []
    sum_l = 0
    for elem in zoz:
        sum_l += elem
        cum_zoz.append(sum_l)
    return cum_zoz


def middle(zoz):
    zoz.pop(0)
    zoz.pop(-1)
    return zoz


def is_ordered(zoz):
    for i in range(len(zoz)-1):
        if ord(str(zoz[i])) > ord(str(zoz[i+1])):
            return False
    return True


def parny_sucet(zoz):
    sum_l = 0
    for i in range(0, len(zoz), 2):
        sum_l += zoz[i]
    return sum_l


def king_of_the_hill(zoz):
    poc = 0
    for i in range(1, len(zoz)-1):
        if zoz[i-1] < zoz[i] > zoz[i+1]:
            poc += 1
    return poc


def different(zoz):
    iny_zoz = []
    for elem in zoz:
        if elem not in iny_zoz:
            iny_zoz.append(elem)
    return len(iny_zoz)


def just_once(zoz):
    poc = 0
    for elem in zoz:
        if zoz.count(elem) == 1:
            poc += 1
    return poc


def is_anagram(w1, w2):
    zoz = []
    for char in w2:
        zoz.append(char)
    for elem in w1:
        if elem not in zoz:
            return False
        zoz.pop(zoz.index(elem))
    if zoz:
        return False
    else:
        return True


print(is_anagram("act", "cat"))
