import math

def e_power(exponent):
    return math.exp(exponent)

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

def iFun(sLast, iLast, beta, gama, miu):
	return (sLast * e_power(-miu) * (1 - e_power(-(beta * iLast))) + (iLast * e_power(-miu) * e_power(-gama)))
    
def s_h(g_h, miu, beta, ro, prev_I, prev_S, prev_R):
    return (g_h + 
            (e_power(-miu) * e_power(beta * prev_I) * prev_S) + 
            (prev_R * e_power(-miu) * (1 - e_power(-ro))) )

def main():
    h = int(input("Introduce el número de poblaciones (h): "))

	for i in range(1,h):
		n = int(input("Introduce el número inicial de individuos de la población: "))
		ch = int(input("Introduce ch: "))
		miu = int(input("Introduce el factor miu (probabilidad de mortalidad del virus): "))
		rho = int(input("Introduce el factor rho: "))
		beta = int(input("Introduce el factor beta: "))
		gamma = int(input("Introduce el factor gamma: "))

		sArray = [0]
		iArray = [0]
		rArray = [0]

		for t in range(1, 150):
			sArray.push(sFun())
			iArray.push(iFun(sArray[t - 1], iArray[t - 1], beta, gama, miu))
			rArray.push(rFun())

main()

