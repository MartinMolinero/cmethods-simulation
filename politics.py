import numpy as np
import random

def calc_c(matrix, vector):
    E = np.array(matrix) * np.array(vector)
    return E.sum()

def get_sum(p, v):
    sum = 0
    for i in range(len(p)):
        sum += p[i] * v[i]
    return sum

def GEPP(A, b, doPricing = True):
    '''
    Gaussian elimination with partial pivoting.

    input: A is an n x n numpy matrix
           b is an n x 1 numpy array
    output: x is the solution of Ax=b 
            with the entries permuted in 
            accordance with the pivoting 
            done by the algorithm
    post-condition: A and b have been modified.
    '''
    n = len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between"+
                         "A & b.", b.size, n)
    # k represents the current pivot row. Since GE traverses the matrix in the 
    # upper right triangle, we also use k for indicating the k-th diagonal 
    # column index.

    # Elimination
    for k in range(n-1):
        if doPricing:
            # Pivot
            maxindex = abs(A[k:,k]).argmax() + k
            if A[maxindex, k] == 0:
                raise ValueError("Matrix is singular.")
            # Swap
            if maxindex != k:
                A[[k,maxindex]] = A[[maxindex, k]]
                b[[k,maxindex]] = b[[maxindex, k]]
        else:
            if A[k, k] == 0:
                raise ValueError("Pivot element is zero. Try setting doPricing to True.")
        #Eliminate
        for row in range(k+1, n):
            multiplier = A[row,k]/A[k,k]
            A[row, k:] = A[row, k:] - multiplier*A[k, k:]
            b[row] = b[row] - multiplier*b[k]
    # Back Substitution
    x = np.zeros(n)
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
    return x

def main():

    # Load files
    P = []
    R = []
    with open("matrix.txt", "r") as f:
        for line in f:
            P.append(np.matrix(line))

    with open("politic.txt", "r") as f:
        for line in f:
            R.append(np.matrix(line))

    # Init required variables

    size = P[0].shape[0]
    actions = len(P)

    c = []
    alpha = float(input("Enter value of alpha: >> "))

    # Calculate Cs
    for i in range(actions):
        for j in range(0, size):
            c.append(calc_c(P[i][j:j+1], R[i][j:j+1]))

    # Print Cs
    for i in range(actions):
        print("Cs of action", i+1)
        for j in range(size):
            print(" ",c[size*i + j])

    # Step 1: random politic
    s = [int(random.random() * actions+1) for i in range(size)]
    prev_s = []
    itr = 0
    while not prev_s == s:
        print("\nS",itr, " = ", s)
        a = []
        b = []
        # Step 2: Calculate vectors
        for i in range(len(s)):
            a.append(np.squeeze(np.asarray(P[s[i]-1][i])))
            aux = []
            aux.append(c[size*(s[i]-1) + i])
            b.append(aux)

        a = np.array(a) * -alpha
        for i in range(size):
            a[i][i] += 1.0
        b = np.array(b)

        print(a)
        print(b)

        v = GEPP(a, b)
        print("\nValor de incógnitas vs(i) y vs(j): ", v)

        v_max = {}
        maxes = {}
        for i in range(actions):
            for j in range(size):
                p = np.squeeze(np.asarray(P[i][j]))
                aux = c[i*size + j] + alpha*(get_sum(p, v))
                if j in maxes and aux > maxes[j]:
                    maxes[j] = aux 
                    v_max[j] = i
                elif not (j in maxes):
                    maxes[j] = aux
                    v_max[j] = i

        new_s = []
        k = []
        for i in range(size):
            new_s.append(v_max[i] + 1)
            k.append(maxes[i])

        print("K = ", k)

        print(s, "==", new_s, "?", s == new_s)
        prev_s = s.copy()
        s = new_s
        itr += 1

if __name__ == "__main__":
    main()
