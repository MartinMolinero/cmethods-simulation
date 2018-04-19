def lines_to_matrix(input, start, end):
    matrix = []
    for i in range(start,int(end)):
        line = input[i].split(',')
        matrix.append(line)
    return matrix

def split_lines_to_actions(input, start, end):
    subarray = []
    return input[start:end]

def main():
    textFile = open("policies.txt",'r')
    lines = textFile.readlines()
    states = int(lines[0])
    actions = int(lines[1])
    input = []
    print('lines', lines)
    for i,line in enumerate(lines):
        if i >1:
            line = str(line).rstrip()
            print(line)
            input.append(line)
    print(input)
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
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
