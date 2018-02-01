#!/usr/bin/python
# encoding: utf-8
import math;

def combination(n,k):
    f = math.factorial
    return f(n) / (f(k) * f(n-k))


def cumulativeBinom():
    res = 0;
    n = input("Introduce el valor de n")
    p = input("Introduce el valor de p")
    q = input("Introduce el valor de q")
    low_limit = input("Introduce el limite inferior")
    upper_limit = input("Introduce el limite superior")
    for x in range(low_limit,upper_limit+1):
        res += combination(n, x) * pow(p,x) * pow(q,n-x)
    return "Result: " + str(res)


def binom():
    n = input("Introduce el valor de n")
    k = input("Introduce el valor de k")
    p = input("Introduce el valor de p")
    q = input("Introduce el valor de q")
    return "Result: " + str(combination(n, k) * pow(p,k) * pow(q,n-k)) + "\nV: " +str(n*p*q) + "\nDesvesta:" +str( math.sqrt(n*p*q))

def poissionfunc():
    return 0
def poissonproc():
    return 1

def printMenu():
    print("1-Distribución binomial\n")
    print("2-Binomial acumulativo\n")
    print("2-Distribución poisson\n")
    print("3-Proceso de poisson\n")

def main():
    while (1):
        printMenu();
        choice = input("\nIntroduce la opción seleccionada \n")
        options = {
            1 : binom,
            2 : cumulativeBinom,
            3 : poissionfunc,
            4: poissonproc,
        }
        if choice in options:
             print ("\n\nresult"+ options[choice]() + "\n\n")
        else:
             pass
             print("Not a function")


    # my code here

if __name__ == "__main__":
    main()
