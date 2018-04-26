import numpy as np

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

def compare_policies(improved_policies, max_min):
    policy = []
    for i in range(len(improved_policies[0])):
        max_value = -10000000000000
        max_index = -1
        min_value = 999999999999
        for j in range(len(improved_policies)):
            if max_min == 1:
                if max(improved_policies[j][i],max_value) > max_value:
                    max_value = max(improved_policies[j][i],max_value)
                    max_index = j+1
            else:
                if min(improved_policies[j][i],min_value) < min_value:
                    min_value = min(improved_policies[j][i],min_value)
                    max_index = j + 1
        policy.append(max_index)
    return policy


def improve_policy(probabilities_matrices, alfa, c_values, v_values):
    improved = []
    ##print("all c's")
    ##print(c_values)
    ##print(probabilities_matrices)
    ##print(v_values)

    for i in range(len(probabilities_matrices)):
        temp = 0
        temp_arr = []
        for j in range(len(probabilities_matrices[i])):
            multi_temp = 0.0
            ##print("DICK")
            for k in range(len(v_values)):
                ##print(i,j,k)
                ##print(probabilities_matrices[i][j][k])
                ##print(v_values[k])
                ##print(float(probabilities_matrices[i][j][k])*float(v_values[k]))
                multi_temp += float(probabilities_matrices[i][j][k])*float(v_values[k])
            ##print("c " + str(c_values[i][j]), str(alfa), str(multi_temp))
            temp = c_values[i][j] + -alfa * multi_temp
            ##print(temp)
            temp_arr.append(temp)
        improved.append(temp_arr)
    return improved


def get_cs(probabilities_matrices, r_matrices, states):
    c_i = []

    for j in range(states):
        temp_c = 0
        for k in range(states):
            ###print(r_matrices[i][j][k])
            temp_c += float(probabilities_matrices[j][k]) *  float(r_matrices[j][k])
        c_i.append(temp_c)
    return c_i

def lines_to_matrix(input, start, end):
    matrix = []
    for i in range(start,int(end)):
        line = input[i].split(',')
        matrix.append(line)
    return matrix

def split_lines_to_actions(input, start, end):
    subarray = []
    return input[start:end]

def distribute_formula(probabilities_matrices, alfa):
    matrix = []
    independent = []
    for i in range(len(probabilities_matrices)):
        ###print(i)
        ###print(probabilities_matrices[i])
        temp_row = []
        temp_value = 0
        for j in range(len(probabilities_matrices)):
            ###print(probabilities_matrices[i][j])
            temp_value =  float(probabilities_matrices[i][j]) * alfa
            if i == j:
                temp_value = 1 + temp_value
            temp_row.append(temp_value)
        ###print(temp_row)
        matrix.append(temp_row)
    matrixNp = np.matrix(matrix)
    return matrixNp



def main():
    textFile = open("policies.txt",'r')
    lines = textFile.readlines()
    states = int(lines[0])
    actions = int(lines[1])
    alfa = -float(lines[2])
    policy = [int(i) for i in lines[3].split(' ')]
    input = []
    v_matrix = []
    improved_policies = []

    for i,line in enumerate(lines):
        if i >3:
            line = str(line).rstrip()
            input.append(line)

    counter = 0
    limit = states * actions
    offset = states * 2
    states_info_array = []

    while counter <= limit:
        states_info_array.append(split_lines_to_actions(input, counter, (counter+offset)))
        counter += offset


    iteration = 0;
    while True:
        probabilities_matrices = []
        r_matrices = []
        cs = []
        distributed_matrices = []
        policy_probs = []
        policy_cs = []
        print(policy)
        #print(iteration)
        for i,states_row in enumerate(states_info_array):
            probabilities_matrices.append(lines_to_matrix(states_info_array[i], 0,states))
            r_matrices.append(lines_to_matrix(states_info_array[i],states,states+states))



        for i in range(actions):
            cs.append(get_cs(probabilities_matrices[i], r_matrices[i], states))

        ##print(probabilities_matrices)


        for i in range(len(policy)):
            policy_probs.append(probabilities_matrices[policy[i] - 1][i])
            policy_cs.append(cs[policy[i] - 1][i])

        ##print(policy_probs)
        ##print(policy_cs)

        distributed_matrices = distribute_formula(policy_probs, alfa)
        #distributed_matrices.append(makeatrix)

        #make gauss jordan shit

        # transform to np
        distributed_matrices = np.array(distributed_matrices)
        policy_cs = np.array(policy_cs)

        ##print(distributed_matrices)
        ##print(policy_cs)

        #hacer que gauss jordan regrese las v(i)
        vs = GEPP(distributed_matrices, policy_cs)
        #solo sacar v_matrix[-1], v_matrix[-2]

        ##print(vs)

        improved_policies = improve_policy(probabilities_matrices, alfa, cs, vs)
        ##print(improved_policies)
        #assuming that we have an array of v's having [[v11, v21, v31], [v12, v22, v32]] this method should work
        iteration += 1
        if policy != compare_policies(improved_policies,1):
            policy = compare_policies(improved_policies,1)
        else:
            break


if __name__ == "__main__":
    # execute only if run as a script
    main()
