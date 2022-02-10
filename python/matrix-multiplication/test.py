import os

def print_matrix(matrix):
    print("input matrix:")
    for row in matrix:
        print(" ".join(row))

def read_matrix_from_file(file_name):
    file_path = os.path.join(os.getcwd(), 'input', file_name)
    user_matrix = list()
    with open(file_path, 'r') as fh:
        all_lines = fh.readlines()
        for line in all_lines:
            if line.strip():
                user_matrix.append(line.strip().split(' '))
    return(user_matrix)

def read_matrix_from_user():
    pass

def matrix_mul(matix1, matrix2):
    # Multily matrix1 and matrix2, and return result matrix.
    matrix = list()
    matrix.append([11, 22, 33])
    return matrix

if __name__ == '__main__':
    '''
    matrix1 = read_matrix_from_file('file001.txt')
    print_matrix(matrix1)
    matrix2 = read_matrix_from_file('file002.txt')
    print_matrix(matrix2)
    '''
    matrix1 = read_matrix_from_user()
    print_matrix(matrix1)
    matrix2 = read_matrix_from_user()
    print_matrix(matrix2)

    result_matrix = matrix_mul(matrix1, matrix2)
    print("matrix multiplication")
    print(result_matrix)
