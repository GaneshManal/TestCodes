import os

def print_matrix(matrix):
    print("input matrix:")
    for row in matrix:
        print(" ".join([str(x) for x in row]))

def read_matrix_from_file(file_name):
    file_path = os.path.join(os.getcwd(), 'input', file_name)
    all_user_matrix = list()
    user_matrix = list()
    with open(file_path, 'r') as fh:
        all_lines = fh.readlines()
        for line in all_lines:
            if line.strip():
                int_list = [ int(x) for x in line.strip().split(' ')]
                user_matrix.append(int_list)
            else:
                all_user_matrix.append(user_matrix)
                user_matrix = list()

        if all_lines[-1].strip():
            print("matrix :", user_matrix)
            all_user_matrix.append(user_matrix)

    print("Number of matrix found: {}".format(len(all_user_matrix)))
    return(all_user_matrix)

if __name__ == '__main__':
    matrix_list = read_matrix_from_file('sample_input.txt')
    for matrix in matrix_list:
        print_matrix(matrix)
    