import math

def miroir(s, indice):
    s1 = s[:indice+1]
    s2 = s1[::-1]
    re = s1 + s2
    return re

def derive(list, interval):
    re = []

    if len(list) <= 1: 
        return False

    for i in range(1, len(list)):
        derive = (list[i] - list[i-1]) / interval
        re.append(derive)

    return re

def derive2(list, interval):
    der1 = derive(list, interval)
    return derive(der1, interval)

def appro_derive(func, ordre, point):
    return -1

    