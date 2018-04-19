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
    matrix = [[]]
    independent = []
    for i in range(len(probabilities_matrices)):
        temp_row = []
        for j in range(len(probabilities_matrices)):
            temp_value =  probabilities_matrices[i][j] * alfa
            if i == j:
                temp_value = 1 - temp_value
            temp_row.append(temp_value)
        matrix[i].append(temp_row)
    return matrixNp = np.matrix(matrix)



def main():
    textFile = open("policies.txt",'r')
    lines = textFile.readlines()
    states = int(lines[0])
    actions = int(lines[1])
    alfa = -float(lines[2])
    input = []

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

    for i,states_row in enumerate(states_info_array):
        probabilities_matrices.append(lines_to_matrix(states_info_array[i], 0,states))
        r_matrices.append(lines_to_matrix(states_info_array[i],states,states+states))

    cs = []
    print("policies")
    print(probabilities_matrices[1])
    print("rs")
    print(r_matrices[1])

    for i in range(actions):
        cs.append(get_cs(probabilities_matrices[i], r_matrices[i], states))
    print(cs)

    distribute_formula(probabilities_matrices, alfa):


if __name__ == "__main__":
    # execute only if run as a script
    main()
