from random import randint

def generate_empty_matrix(n):
    mat = []
    for f in range(n):
        mat.append([0] * n)
    return mat

def fill_with_binary(matrix, limit, n):
    counter = 0
    while(counter < limit):
        r1  = randint(0,n)
        r2 = randint(0,n)
        if( r1 != r2 and matrix[r1][r2] != 1):
            matrix[r1][r2] = 1
            counter+=1
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
    print ("Max es " +  str(max) + " unos en la fila " + str(max_aux))
    print ("Min es " +  str(min) + " unos en la fila " + str(min_aux))



n = input("Introduce el tamano de la matriz\n")
mat = generate_empty_matrix(n)
perc = input("Introduce el porcentaje deseado\n")
tam = n*n
ones = round(tam * ( float(perc) / 100.0))
mat  = fill_with_binary(mat, ones, n-1)
print(mat)
c_array = count_ones(mat)
max_and_min(c_array)
