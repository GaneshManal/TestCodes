'''
Author: Ganesh Manal
Example code: Sorting arrays
'''

def bubble_sort(num_list):
    '''
    sort the array using the bubble sort technique
    '''
    for i in range(len(array)):
        swapping_done = False
        for j in range(i+1, len(array)):
            if num_list[i] > num_list[j]:
                # Swap the numbers
                swapping_done = True
                num_list[i], num_list[j] = num_list[j], num_list[i]
        if not swapping_done:
            break
        # print(num_list)
    return True


if __name__ == "__main__":
    test_arrays = [
        [2, 5, 3, 1],
        [7, 6, 5, 4, 3, 2, 1],
        [11, 12, 13, 14, 15],
    ]

    for array in test_arrays:
        print(f"actual array: {array}")
        bubble_sort(array)
        print(f"sorted array: {array}")
