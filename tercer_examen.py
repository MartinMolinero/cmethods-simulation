from random import randint
import sys
#import numpy as np
#np.set_printoptions(threshold='nan')

def generate_empty_matrix(n):
    mat = []
    for f in range(n):
        mat.append([0] * n)
    #mat = np.zeros(shape=(n,n))
    return mat

def fill_with_binary_a(matrix, limit, n):
    counter = 0
    while(counter < limit):
        r1  = randint(0,n)
        r2 = randint(0,n)
        if( r1 != r2 and matrix[r1][r2] != 1):
            matrix[r1][r2] = 1
            counter+=1
    return matrix

def fill_with_binary_b(matrix, limit, n):
    counter = 0
    while(counter < limit):
        r1  = randint(0,n)
        r2 = randint(0,n)
        if( r1 != r2 and matrix[r1][r2] != 1):
            matrix[r1][r2] = 1
            matrix[r2][r1] = 1
            counter+=2
    return matrix

def count_ones(matrix):
    counters = []
    for f in range(len(matrix)):
        counter = 0
        for c in range(len(matrix[f])):
            if(matrix[f][c] == 1):
                counter +=1
        counters.append(counter)
    return(counters)

def max_and_min(counters):
    max = -1
    min = 10000000000000000000000000
    max_aux = 0
    min_aux = 0
    for i in range(len(counters)):
        if(counters[i] > max):
            max = counters[i]
            max_aux = i
        elif(counters[i] < min):
            min = counters[i]
            min_aux = i
    print ("\nMáximos y mínimos por fila:")
    print ("Max es " +  str(max) + " unos en la fila " + str(max_aux))
    print ("Min es " +  str(min) + " unos en la fila " + str(min_aux))

def print_mat(matrix):
    print('\n'.join([' '.join(['{:1}'.format(item) for item in row]) 
      for row in matrix]))
    

def matriz_a():
    n = int(input("\nIntroduce el número de renglones/columnas de la matriz cuadrada\n"))
    mat = generate_empty_matrix(n)
    perc = input("\nIntroduce el porcentaje deseado\n")
    size = n*n
    ones = round(size * ( float(perc) / 100.0))
    
    print("\nP="+str(ones))
    mat  = fill_with_binary_a(mat, ones, n-1)
    #print(np.matrix(mat))
    print("\nMatriz:")
    print_mat(mat)
    c_array = count_ones(mat)
    max_and_min(c_array)


def matriz_b():
    n = int(input("\nIntroduce el número de renglones/columnas de la matriz cuadrada\n"))
    mat = generate_empty_matrix(n)
    perc = input("\nIntroduce el porcentaje deseado\n")
    size = n*n
    ones = round(size * ( float(perc) / 100.0))
    
    print("\nP="+str(ones))
    mat  = fill_with_binary_b(mat, ones, n-1)
    #print(np.matrix(mat))
    print("\nMatriz:\n")
    print_mat(mat)
    c_array = count_ones(mat)
    max_and_min(c_array)


def main():
    while(True):
        mat_name = str(input("\nIntroduce la matríz que desea generar: (a) ó (b), (0) para terminar.\n"))
        if(mat_name == 'a' or mat_name == 'A'):
            matriz_a()
        elif(mat_name == 'b'or mat_name == 'B'):
            matriz_b()
        elif(mat_name == '0'):
            break
        else:
            print("Valor introducido inválido, introducir (a), (b), o (0)")

if __name__ == "__main__":
    main()
