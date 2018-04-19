import math
import sys
#sys.path.append("/Users/BernardoOrtega/anaconda/lib/python3.5/site-packages")
import matplotlib.pyplot as plt
import numpy as np


def e_power(exponent):
    return math.exp(exponent)

def gh_1(rh, miuh, nht, ch):
    return rh * e_power(-miuh)*nht*(1- ((e_power(-miuh)*nht)/(ch)))

def nh_1_next_time(rh, miuh, nht, ch):
    return (rh * e_power(-miuh) * nht * (1- ((e_power(-miuh)*nht)/(ch))) +
            (e_power(-miuh) * nht))

def gh_2(miuh, nh):
    gh =  (1 - e_power(-miuh)) * nh
    return gh

def nh_2_next_time(nh):
    return nh

def iFun(sLast, iLast, beta, gama, miu):
	i = (sLast * (e_power(-miu)) * (1 - e_power(-(beta * iLast)))) + (iLast * e_power(-miu) * e_power(-gama))
	return i

def sFun(g_h, miu, beta, rho, prev_I, prev_S, prev_R):
    s = (g_h +
            (e_power(-miu) * e_power(-(beta * prev_I)) * prev_S) +
            (prev_R * e_power(-miu) * (1 - e_power(-rho))))
    return s

def rFun(prev_R, miuh, rohi, prev_I, gamahi):
    return (prev_R * e_power(-miuh) * e_power(-rohi)) + (prev_I * e_power(-miuh) * (1 - e_power(-gamahi)))


def main():
    # debug_mode = false para pedir inputs a usuario
    debug_mode = True
    
    if debug_mode:
        h = 2
        T = 40
    else:    
        h = int(input("Introduce el número de poblaciones (h): "))
        # T = 150
        T = int(input("Introduce el periodo de tiempo a simular (T): "))
    
    # Fill arrays with ceros
    sArray = [[0.0 for i in range(T)] for i in range(h)]
    iArray = [[0.0 for i in range(T)] for i in range(h)]
    rArray = [[0.0 for i in range(T)] for i in range(h)]

    for i in range(0,h):
        if debug_mode:
            n = 1000
            if(i == 0):
                # ch tiene que ser un número mayor que n
                ch = 1100
            miu = 0.4
            rho = 0.6
            beta = 0.5
            gamma = 0.4
        else:
            n = float(input("Introduce el número inicial de individuos de la población: "))
            if(i == 0):
                ch = int(input("Introduce ch (mayor que n): "))
            miu = float(input("Introduce el factor miu (probabilidad de mortalidad del virus): "))
            rho = float(input("Introduce el factor rho: "))
            beta = float(input("Introduce el factor beta: "))
            gamma = float(input("Introduce el factor gamma: "))
            
        

        sArray[i][0] = (n - 1)
        iArray[i][0] = 1.0
        rArray[i][0] = 0.0
        
        indexes = []
        for t in range(1, T):
            if(i == 0):
                n = nh_1_next_time(rho, miu, n, ch)
                g = gh_1(rho, miu, n, ch)
            else:
                g = gh_2(miu, n)
                
            sArray[i][t] = (sFun(g, miu, beta, rho, iArray[i][t - 1], sArray[i][t - 1], rArray[i][t - 1]))
            iArray[i][t] = (iFun(sArray[i][t - 1], iArray[i][t - 1], beta, gamma, miu))
            rArray[i][t] = (rFun(rArray[i][t - 1], miu, rho, iArray[i][t - 1], gamma))
            indexes.append(t)
            
        indexes.append(T)
        
        print("\nResultados de la población "+ str(i+1))
        plt.plot(indexes, sArray[i], 'r', indexes, iArray[i], 'b', indexes, rArray[i], 'g')
        plt.show()
        print("Rojo = Suseptibles \t Azul = Infectados \t Verde = Recuperados")
        print("\n")        
    
main()

#*
