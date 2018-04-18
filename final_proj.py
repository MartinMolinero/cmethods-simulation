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
    h = int(input("Introduce el número de poblaciones (h): "))

    for i in range(0,h):
        n = float(input("Introduce el número inicial de individuos de la población: "))
        #ch = int(input("Introduce ch: "))
        miu = float(input("Introduce el factor miu (probabilidad de mortalidad del virus): "))
        rho = float(input("Introduce el factor rho: "))
        beta = float(input("Introduce el factor beta: "))
        gamma = float(input("Introduce el factor gamma: "))

        sArray = [n - 1]
        iArray = [1.0]
        rArray = [0.0]
        indexes = []
        for t in range(1, 150):
            #n = nh_next_time(rho, miu, n, ch)
            #g = gh_1(rho, miu, n, ch)
            g = gh_2(miu, n)

            sArray.append(sFun(g, miu, beta, rho, iArray[t - 1], sArray[t - 1], rArray[t - 1]))
            iArray.append(iFun(sArray[t - 1], iArray[t - 1], beta, gamma, miu))
            rArray.append(rFun(rArray[t - 1], miu, rho, iArray[t - 1], gamma))
            indexes.append(t)
        indexes.append(150)

        first_index = 50
        second_index = 100
        third_index = 150
        '''
        temp_array_50 = []
        temp_array_50.append(sArray[first_index -1])
        temp_array_50.append(iArray[first_index -1])
        temp_array_50.append(rArray[first_index -1])
        temp_array_100 = []
        temp_array_100.append(sArray[second_index -1])
        temp_array_100.append(iArray[second_index -1])
        temp_array_100.append(rArray[second_index -1])
        temp_array_150 = []
        temp_array_150.append(sArray[third_index -1])
        temp_array_150.append(iArray[third_index -1])
        temp_array_150.append(rArray[third_index -1])
        temp_s = []
        temp_s.append(sArray[first_index -1])
        temp_s.append(sArray[second_index -1])
        temp_s.append(sArray[third_index -1])
        temp_i = []
        temp_i.append(iArray[first_index -1])
        temp_i.append(iArray[second_index -1])
        temp_i.append(iArray[third_index -1])
        temp_r = []
        temp_r.append(rArray[first_index -1])
        temp_r.append(rArray[second_index -1])
        temp_r.append(rArray[third_index -1])


        print("\n")
        print(sArray)
        print(sArray[first_index-1],sArray[second_index -1], sArray[third_index -1])
        print("\n")
        print(iArray)
        print(iArray[first_index-1],iArray[second_index -1], iArray[third_index -1])
        print("\n")
        print(rArray)
        print(rArray[first_index-1],rArray[second_index -1], rArray[third_index -1])

        print(temp_s)
        print(temp_i)
        print(temp_r)

        print (temp_array_50)
        print (temp_array_100)
        print (temp_array_150)
        '''
        plt.plot(indexes, sArray, 'r', indexes, iArray, 'b', indexes, rArray, 'g')
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
