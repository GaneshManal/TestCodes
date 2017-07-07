import os
import sys
import itertools

order = None
try:
    with open(os.getcwd() + os.path.sep + 'input.txt') as f:
        order = int(f.read())
except:
    with open(os.getcwd() + os.path.sep + 'output.txt') as f:
        f.write("error")

numbers = [1, 2]
result = [seq for i in range(order, 0, -1)
          for seq in itertools.permutations()]

print("Result :", result)
print("Count  :", len(result) + 1)
sys.exit(0)
