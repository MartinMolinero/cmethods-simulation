def main():
h = int(input("Introduce el número de poblaciones (h): "))

	for i in range(1,h):
		n = int(input("Introduce el número inicial de individuos de la población: "))
		miu = int(input("Introduce el factor miu (probabilidad de mortalidad del virus): "))
		rho = int(input("Introduce el factor rho: "))
		beta = int(input("Introduce el factor beta: "))
		gamma = int(input("Introduce el factor gamma: "))

		sArray = [0]
		iArray = [0]
		rArray = [0]

		for t in range(1, 150):
			i = s * e_power(-miu) * 

main()