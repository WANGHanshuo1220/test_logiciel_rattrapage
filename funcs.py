import math

def miroir(s, indice):
    s1 = s[:indice+1]
    s2 = s1[::-1]
    re = s1 + s2
    return re

# “list” est l'ensemble des positions des boules à un moment donné
# “interval” est l'intervalle d'échantillonnage.
def derive(list, interval):
    re = []

    if len(list) <= 1: 
        return False

    for i in range(1, len(list)):
        derive = (list[i] - list[i-1]) / interval
        re.append(derive)

    return re
# Renvoie les vitesses moyennes d'un objet en mouvement (dérivée de premier ordre)


def derive2(list, interval):
    der1 = derive(list, interval)
    if der1:
        return derive(der1, interval)
    else:
        return False
        

def appro_derive(func, point, ordre):
    re = func(point)
    a = len(str(ordre).split(".")[1])
    re = round(re, a)
    return re


def func_x2(x):
    return pow(x, 2)


def func_polynomial(x):
    return pow(x, 3) + 2 * pow(x, 2) + 3 * x + 1


def func_x_1(x):
    if x != 0:
        return 1/x
    else:
        return False 


def func_sin(x):
    return math.sin(x)

    