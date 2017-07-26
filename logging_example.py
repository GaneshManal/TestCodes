import logging
# DEBUG / INFO / WARNING / ERROR / CRITICAL
"""
    Default Log level - Warning
    Default Log Output - Console
    Log Record attributes -  
"""

# Filename if want output in file
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    """Add Function"""
    return x + y


num1, num2 = 10, 20
add_result = add(num1, num2)
logging.debug("Addition: {} + {} = {}".format(num1, num2, add_result))
