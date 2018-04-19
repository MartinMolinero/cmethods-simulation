import numpy as np
from gauss import GEPP

def compare_policies(improved_policies, max_min):
    policy = []
    max_value = -10000000000000
    min_value = 999999999999
    for i in range(len(improved_policies)):
        for j in range(len(improved_policies[0])):
            if max_min == 1:
                max_value = max(improved_policies[j][i],max_value)
            else:
                min_value = min(improved_policies[j][i],min_value)
        policy.append(j)

    return policy


def improve_policy(probabilities_matrices, alfa, c_values, v_values):
    improved = []

    for i in range(len(probabilities_matrices)):
        for j in range(probabilities_matrices[i]):
            temp = 0
            multi_temp = 0
            for k in range(v_values):
                multi_temp += (probabilities_matrices[i][j][k] * v_values[i][j][k])
            temp = c[i][k] + (alfa * multi_temp)
        improved.append(temp)
    return improved


def get_cs(probabilities_matrices, r_matrices, states):
    c_i = []

    for j in range(states):
        temp_c = 0
        for k in range(states):
            #print(r_matrices[i][j][k])
            temp_c += float(probabilities_matrices[j][k]) *  float(r_matrices[j][k])
        c_i.append(temp_c)
    print(temp_c,float(probabilities_matrices[j][k]) , float(r_matrices[j][k]))
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
        #print(i)
        #print(probabilities_matrices[i])
        temp_row = []
        temp_value = 0
        for j in range(len(probabilities_matrices)):
            #print(probabilities_matrices[i][j])
            temp_value =  float(probabilities_matrices[i][j]) * alfa
            if i == j:
                temp_value = 1 - temp_value
            temp_row.append(temp_value)
        #print(temp_row)
        matrix.append(temp_row)
    matrixNp = np.matrix(matrix)
    return matrixNp



def main():
    textFile = open("policies.txt",'r')
    lines = textFile.readlines()
    states = int(lines[0])
    actions = int(lines[1])
    alfa = -float(lines[2])
    input = []
    v_matrix = []
    improved_policies = []
    k_matrix  = [[-1,-1,-1]]

    for i,line in enumerate(lines):
        if i >2:
            line = str(line).rstrip()
            input.append(line)

    counter = 0
    limit = states * actions
    offset = states * 2
    states_info_array = []

    while counter <= limit:
        states_info_array.append(split_lines_to_actions(input, counter, (counter+offset)))
        counter += offset

    probabilities_matrices = []
    r_matrices = []

    while True:
        for i,states_row in enumerate(states_info_array):
            probabilities_matrices.append(lines_to_matrix(states_info_array[i], 0,states))
            r_matrices.append(lines_to_matrix(states_info_array[i],states,states+states))

        cs = []

        for i in range(actions):
            cs.append(get_cs(probabilities_matrices[i], r_matrices[i], states))
        print(cs)
        distributed_matrices = []
        for i in range(actions):
            matrix = distribute_formula(probabilities_matrices[i], alfa)
            distributed_matrices.append(matrix)

        print(distributed_matrices)
        #make gauss jordan shit

        for i in range(len(distributed_matrices)):
            #hacer que gauss jordan regrese las v(i)
            vs = GEPP(distributed_matrices, cs)
            v_matrix.append(vs)
            #solo sacar v_matrix[-1], v_matrix[-2]
        improved_policies.append(improve_policy(probabilities_matrices, alfa, c_values, v_values))
        #assuming that we have an array of v's having [[v11, v21, v31], [v12, v22, v32]] this method should work
        k_matrix.append(compare_policies(improved_policies))


if __name__ == "__main__":
    # execute only if run as a script
    main()
