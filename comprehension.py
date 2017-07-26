import sys

# List Comprehension
squares = [x*x for x in range(1, 11)]
print "List Comprehension: ", squares

# Dictionary Comprehension
numbers = [1, 2, 3]
counts = ["one", "two", "three"]
count_dict = { num: count for num, count in zip(numbers, counts)}
print "Dict Comprehension: ", count_dict

# Set Comprehension
nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
set_x = {x for x in nums}
print "Set Comprehension: ", set_x

# Generator Comprehension
nums = range(1,6)
gen_x = (n*n for n in nums)
print "Gen Comprehension: ",
for x in gen_x:
    print x,

sys.exit(0)

