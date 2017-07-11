matrix = [
    [None, None, None, None, 4, None, None, None, None, None],
    [None, None, 5, 1, 2, 0, 5, 1, None, None],
    [None, 1, 4, 2, 4, 8, 5, None, None, None],
    [None, None, 8, 0, 7, 6, 9, None, None, None],
    [None, None, None, 3, 4, 2, 3, 4, 2, 1],
    [9, 2, 7, 8, 0, 9, 0, None, None, None],
    [None, None, None, None, 1, 7, 9, 3, None, None],
    [None, None, None, 4, 2, 3, None, None, None, None],
    [None, None, None, 9, 8, 4, 9, None, None, None],
    [None, 1, 5, 0, 6, None, None, None, None, None],
    [None, None, None, None, 8, None, None, None, None, None]
]

row_count = len(matrix)
col_count = len(matrix[0])
print 'row count :', row_count, col_count, matrix[0]
h_numbers = []
for row in range(0, row_count):
    # noinspection PyInterpreter
    for col in range(0, col_count):
        if matrix[row][col] is not None:

            x_number = matrix[row][col]

            if x_number not in h_numbers:
                h_numbers.append(x_number)

            for x in range(col+1, col_count):
                if matrix[row][x] is not None:
                    x_number = x_number*10 + matrix[row][x]
                    if x_number not in h_numbers:
                        h_numbers.append(x_number)

                        rev_num = int(str(x_number)[::-1])
                        if rev_num not in h_numbers:
                            h_numbers.append(rev_num)

print "Horizontal Numbers :", h_numbers

v_numbers = []
for row in range(0, row_count):
    for col in range(0, col_count):
        if matrix[row][col] is not None:

            x_number = matrix[row][col]
            if x_number not in v_numbers:
                v_numbers.append(x_number)

            for x in range(row+1, row_count):
                if matrix[x][col] is not None:
                    x_number = x_number*10 + matrix[x][col]
                    if x_number not in v_numbers:
                        v_numbers.append(x_number)

                        rev_num = int(str(x_number)[::-1])
                        if rev_num not in v_numbers:
                            v_numbers.append(rev_num)

print "Vertical Numbers :", v_numbers

d_numbers = []
for row in range(0, len(matrix)):
    for col in range(0, len(matrix[row])):
        if matrix[row][col] is not None:
            x_number = matrix[row][col]

            if x_number not in d_numbers:
                d_numbers.append(x_number)

            dx = 1
            while row + dx <= row_count-1 and col + dx <= col_count-1:
                if matrix[row+dx][col+dx] is not None:
                    x_number = x_number*10 + matrix[row+dx][col+dx]
                    if x_number not in d_numbers:
                        d_numbers.append(x_number)

                        rev_num = int(str(x_number)[::-1])
                        if rev_num not in d_numbers:
                            d_numbers.append(rev_num)
                    dx += 1
                else:
                    break

            dx, x_number = 1, matrix[row][col]
            while row + dx <= row_count-1 and col - dx >= 0:
                if matrix[row+dx][col-dx] is not None:
                    x_number = x_number*10 + matrix[row+dx][col-dx]
                    if x_number not in d_numbers:
                        d_numbers.append(x_number)

                        rev_num = int(str(x_number)[::-1])
                        if rev_num not in d_numbers:
                            d_numbers.append(rev_num)
                    dx += 1
                else:
                    break

print "Diagonal Numbers :", d_numbers

h_numbers.extend(v_numbers)
h_numbers.extend(d_numbers)
print "All Numbers :", h_numbers

import math
max = 0
for each_number in h_numbers:
    #print 'Numebr :', each_number, round(math.pow(each_number, (1.0 / 3))), math.pow(int(round(
    # math.pow(each_number, (1.0/3)))), 3)
    if each_number == math.pow(int(round(math.pow(each_number, (1.0/3)))), 3):
        print 'Numebr :', each_number, math.pow(int(round(math.pow(each_number, (1.0/3)))), 3)
        if max < each_number:
            max = each_number

print "Maximum : ", max

