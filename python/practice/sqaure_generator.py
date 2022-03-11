# Generator Function for generating square of numbers
def square_numbers(nums):
    for num in nums:
        yield num*num


numbers = range(1, 6)
gen_x = square_numbers(numbers)
print "Generator Object : ", gen_x
print "Generator Mem   : ", dir(gen_x)

""""
'print '--->', gen_x.next()
print '--->', gen_x.next()
print '--->', gen_x.next()
print '--->', gen_x.next()
print '--->', gen_x.next()
# print '--->', gen_x.next() # StopIteration Exception.
"""

# print list(gen_x)

for num in gen_x:
    print num,
