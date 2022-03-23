'''
Author: Ganesh Manal
Example code: Sorting arrays
'''
import time


def bubble_sort(num_list):
    '''
    sort the array using the bubble sort technique
    '''
    size = len(array)
    for i in range(size-1):
        # print(f"iteration: {i+1}")
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
        # [x for x in range(100, 0, -1)],
        # [x for x in range(50, 0, -1)],
        # [x for x in range(40, 0, -1)],
        # [x for x in range(30, 0, -1)],
        # [x for x in range(20, 0, -1)],
        # [x for x in range(10, 0, -1)],
        # [x for x in range(5, 0, -1)],
        [2, 5, 3, 1],
        [7, 6, 5, 4, 3, 2, 1],
        [11, 12, 13, 14, 15],
    ]

    for array in test_arrays:
        # print(f"actual array: {array}")
        print("array size: {}".format(len(array)))
        start_time = time.time()
        bubble_sort(array)
        end_time = time.time()
        print("execution time: {}".format(end_time-start_time))
        # print(f"sorted array: {array}")
