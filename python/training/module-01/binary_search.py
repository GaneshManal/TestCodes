'''
Author: Ganesh Manal
Example code: Binary search - using iterative approach
'''

def binary_search(num_list, search_number):
    '''
    search the number using binary search
    input: numbers list, number to search
    return: index of number in list
    '''
    start_index, last_index = 0, len(num_list)-1
    while start_index <= last_index:
        mid_index = (start_index + last_index) // 2
        # print(f"begin - start: {start_index}, last: {last_index}, mid: {mid_index}")

        if num_list[mid_index] > search_number:
            last_index = mid_index - 1
        elif num_list[mid_index] < search_number:
            start_index = mid_index + 1
        else:
            return mid_index
        # print(f"end - start: {start_index}, last: {last_index}, mid: {mid_index}")
    return -1


if __name__ == "__main__":
    test_arrays = [
        [1, 2, 3, 5],
        [1, 2, 3, 4, 5, 6, 7],
        [11, 12, 13, 14, 15],
        [1, 2, 8, 9],
        [1],
        [2, 3, 4],
        [5]
    ]
    search_numbers = [1, 2, 14, 15, 1, 5, 6]

    for array, number in zip(test_arrays, search_numbers):
        found_index = binary_search(array, number)
        print(f"find number: {number} in array: {array}, found at: {found_index}")
