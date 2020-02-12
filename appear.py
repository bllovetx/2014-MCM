from random import random, randrange
from math import factorial
from car import Car




def comb(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def init_appear(settings):
    settings.add_p = []
    n = settings.max_speed - settings.min_speed
    time_unit = settings.time_unit
    assert time_unit <= 0.1, "time_unit may cause error"
    settings.random_0 = randrange(0, 18)
    settings.random_1 = randrange(0, 18)
    settings.random_2 = randrange(0, 18)
    lamb = 17.6
    sump = 0
    for i in range(0, n):
        p_n = comb(n, i) * ((lamb/n)**i) * ((1-lamb/n)**(n-i))
        sump += p_n
        settings.add_p.append(sump)


def appear(q, time, settings):
    if settings.traffic == 'light':
        if (time - settings.random_0) % 22.3 == 0:
            q.append(Car(settings, speed(settings), 0))
    if settings.traffic == 'heavy':
        if (time - settings.random_0) % 18 == 0:
            q.append(Car(settings, speed(settings), 0))
        if (time - settings.random_1) % 18 == 0:
            q.append(Car(settings, speed(settings), 1))
        if (time - settings.random_2) % 64.6 == 0:
            q.append(Car(settings, speed(settings), 2))

def speed(settings):
    randnum = random()
    i = 0 
    while i < len(settings.add_p):
        if randnum <= settings.add_p[i]:
            break
        i += 1
    return (i + settings.min_speed)/3.6



