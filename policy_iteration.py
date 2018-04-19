def get_cs(policies_matrices, r_matrices, states):
    c_i = []
    for j in range(states):
        temp_c = 0
        for k in range(states):
            #print(r_matrices[i][j][k])
            temp_c += float(policies_matrices[j][k]) *  float(r_matrices[j][k])
        c_i.append(temp_c)
    print(temp_c,float(policies_matrices[j][k]) , float(r_matrices[j][k]))
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

def distribute_formula(policies_matrices, c_values, alfa):
    matrix = []
    for i,row in enumerate(policies_matrices):
        temp_row = []
        temp_value =  c_values[i] + ()

    pass


def main():
    textFile = open("policies.txt",'r')
    lines = textFile.readlines()
    states = int(lines[0])
    actions = int(lines[1])
    alfa = float(lines[2])
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
    policies_matrices = []
    r_matrices = []

    for i,states_row in enumerate(states_info_array):
        policies_matrices.append(lines_to_matrix(states_info_array[i], 0,states))
        r_matrices.append(lines_to_matrix(states_info_array[i],states,states+states))
    cs = []
    print("policies")
    print(policies_matrices[1])
    print("rs")
    print(r_matrices[1])
    for i in range(actions):
        cs.append(get_cs(policies_matrices[i], r_matrices[i], states))
    print(cs)




if __name__ == "__main__":
    # execute only if run as a script
    main()
