#!/usr/bin/python
# encoding: utf-8
import math

def factorial():
    n = int(input("Introduce el valor de n: "))
    return factorial_in(n)

def factorial_in(n):
    acum = 1
    while True:
        if ( n == 0 or n == 1):
            return acum
        else:
            acum = acum * n
            n = n - 1


def combination():
    n = int(input("Introduce el valor de n: "))
    k = int(input("Introduce el valor de k: "))
    return combination_in(n,k)

def combination_in(n,k):
    f = factorial_in
    return f(n) / (f(k) * f(n-k))

def permutation():
    n = int(input("Introduce el valor de n: "))
    k = int(input("Introduce el valor de k: "))
    return permutation_in(n,k)

def permutation_in(n,k):
    f = factorial_in
    return f(n) / f(n-k)


def cumulativeBinom():
    res = 0;
    n = float(input("Introduce el valor de n: "))
    p = float(input("Introduce el valor de p: "))
    q = float(input("Introduce el valor de q: "))
    low_limit = int(input("Introduce el limite inferior: "))
    upper_limit = int(input("Introduce el limite superior: "))
    for x in range(low_limit,upper_limit + 1):
        res += combination_in(n, x) * pow(p,x) * pow(q,n-x)
        print(res)
    return str(res)


def binom():
    n = float(input("Introduce el valor de n: "))
    k = float(input("Introduce el valor de k: "))
    p = float(input("Introduce el valor de p: "))
    q = float(input("Introduce el valor de q: "))
    return str(combination_in(n, k) * pow(p,k) * pow(q,n-k)) + "\nVarianza: " +str(n*p*q) + "\nDesviación estándar:" +str( math.sqrt(n*p*q))

def poisson():
    e = math.e
    x = float(input("Introduce el valor de x: "))
    l = float(input("Introduce el valor de lambda: "))
    res = (pow(e, -l) * pow(l, x)) / factorial_in (x)
    return str(res)

def poissonproc():
    e = math.e
    x = float(input("Introduce el valor de x: "))
    a = float(input("Introduce el valor de alfa: "))
    t = float(input("Introduce el valor de t (tiempo, área, etc): "))
    l = a * t
    res = (pow(e, -l) * pow(l, x)) / factorial_in (x)
    return str(res)

def cumulativePoisson():
    res = 0;
    e = math.e
    l = float(input("Introduce el valor de lambda: "))
    low_limit = int(input("Introduce el limite inferior: "))
    upper_limit = int(input("Introduce el limite superior: "))
    for x in range(low_limit,upper_limit + 1):
        res += (pow(e, -l) * pow(l, x)) / factorial_in (x)
        print(res)
    return str(res)


def printMenu():
    print("1-Distribución Binomial\n")
    print("2-Binomial acumulativo\n")
    print("3-Distribución Poisson\n")
    print("4-Proceso de Poisson\n")
    print("5-Poisson acumulativo\n")
    print("6-Factorial\n")
    print("7-Combinación\n")
    print("8-Permutación\n")

def main():
    while (1):
        printMenu();
        choice = int(input("\nIntroduce la opción deseada \n"))
        options = {
            1: binom,
            2: cumulativeBinom,
            3: poisson,
            4: poissonproc,
            5: cumulativePoisson,
            6: factorial,
            7: combination,
            8: permutation
        }

        if choice in options:
             print ("\n\nResultado: "+ str(options[choice]()) + "\n\n")
        else:
             pass
             print("\n Esa opción no existe. Elige otra: \n")


    # my code here

if __name__ == "__main__":
    main()
