'''
Author: Ganesh Manal
Example code: Sorting arrays
'''

def bubble_sort(num_list):
    '''
    sort the array using the bubble sort technique
    '''
    size = len(array)
    for i in range(size-1):
        swapping_done = False
        for j in range(size-i-1):
            if num_list[j] > num_list[j+1]:
                # Swap the numbers
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                swapping_done = True
                # print(num_list)

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
