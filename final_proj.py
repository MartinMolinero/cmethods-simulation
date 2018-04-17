import math

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
        
        for t in range(1, 150):
            #n = nh_next_time(rho, miu, n, ch)
            #g = gh_1(rho, miu, n, ch)
            g = gh_2(miu, n)
            sArray.append(sFun(g, miu, beta, rho, iArray[t - 1], sArray[t - 1], rArray[t - 1]))
            iArray.append(iFun(sArray[t - 1], iArray[t - 1], beta, gamma, miu))
            rArray.append(rFun(rArray[t - 1], miu, rho, iArray[t - 1], gamma))

        print("\n")
        print(sArray)
        print("\n")
        print(iArray)
        print("\n")
        print(rArray)
        
main()

