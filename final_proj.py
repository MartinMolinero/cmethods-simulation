import math
import sys
#sys.path.append("/Users/BernardoOrtega/anaconda/lib/python3.5/site-packages")
import matplotlib.pyplot as plt
import numpy as np


def e_power(exponent):
    return math.exp(exponent)

def gh_1(rh, miuh, nht, ch):
    return rh * math.exp(miuh)*nht*(1- ((math.exp(miuh)*nht)/(ch)))

def nh_next_time(rh, miuh, nht, ch):
    return (rh * math.exp(miuh) * nht * (1- ((math.exp(miuh)*nht)/(ch))) +
            (math.exp(miuh) * nht))

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


    #miu = 7.8693

    return s

def rFun(prev_R, miuh, rohi, prev_I, gamahi):
    return (prev_R * e_power(-miuh) * e_power(-rohi)) + (prev_I * e_power(-miuh) * (1 - e_power(-gamahi)))


def main():
    # h = int(input("Introduce el número de poblaciones (h): "))
    h = 2
    T = 150
    
    # Fill arrays with ceros
    sArray = [[0 for i in range(T)] for i in range(h)]
    iArray = [[0 for i in range(T)] for i in range(h)]
    rArray = [[0 for i in range(T)] for i in range(h)]

    for i in range(0,h):
        #n = float(input("Introduce el número inicial de individuos de la población: "))
        n = 1000
        if(i == 0):
            # ch tiene que ser un número mayor que n
            # ch = int(input("Introduce ch: "))
            ch = 1100
        '''
        miu = float(input("Introduce el factor miu (probabilidad de mortalidad del virus): "))
        rho = float(input("Introduce el factor rho: "))
        beta = float(input("Introduce el factor beta: "))
        gamma = float(input("Introduce el factor gamma: "))
        '''
        miu = 0.4
        rho = 0.6
        beta = 0.5
        gamma = 0.4

        sArray[i][0] = [n - 1]
        iArray[i][0] = [1.0]
        rArray[i][0] = [0.0]
        
        indexes = []
        for t in range(1, T):
            if(i == 0):
                n = nh_next_time(rho, miu, n, ch)
                g = gh_1(rho, miu, n, ch)
            else:
                g = gh_2(miu, n)

            sArray[i][t] = (sFun(g, miu, beta, rho, iArray[i][t - 1], sArray[i][t - 1], rArray[i][t - 1]))
            iArray[i][t] = (iFun(sArray[i][t - 1], iArray[i][t - 1], beta, gamma, miu))
            rArray[i][t] = (rFun(rArray[i][t - 1], miu, rho, iArray[i][t - 1], gamma))
            indexes.append(t)
            
        indexes.append(150)
        
        plt.plot(indexes, sArray[i], 'r', indexes, iArray[i], 'b', indexes, rArray[i], 'g')
        #plt.plot(indexes, sArray, 'ro')
        #plt.plot(indexes, iArray, 'bs')
        #plt.plot(indexes, rArray, 'g^')
        #esto es para graficar los tres valores de s, i, r en los tiempos 50, 100, 150 por separado
        #plt.plot([first_index, second_index, third_index], temp_array_50, 'b^')
        #plt.plot([first_index, second_index, third_index], temp_array_100, 'go')
        #plt.plot([first_index, second_index, third_index], temp_array_150, 'gs')
        # red dashes, blue squares and green triangles
        plt.show()
main()

#*
