import math


def rh(rh_prev, miuh, rohi, ihi, gamahi):
    return (rh_prev*math.exp(miuh)*math.exp(rohi)) + (ihi*math.exp(miuh)*(1-math.exp(gamahi)))


def gh_1(rh, miuh, nht, ch):
    return rh * math.exp(miuh)*nht*(1- ((math.exp(miuh)*nht)/(ch)))

def nh_next_time():
    return (rh * math.exp(miuh) * nht* (1- ((math.exp(miuh)*nht)/(ch))) + (math.exp(miuh) * nht))

def gh_2(miuh, nh):
    return (1- math.exp(miuh) * nh)

def nh_2_next_time(nh):
    return nh
