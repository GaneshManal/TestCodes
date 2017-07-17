import logging_example
import time
from functools import wraps


def my_logger(original_function):

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging_example.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging_example.INFO)
        logging_example.info('Function called with arguments args {}, kwargs {}'.format(args, kwargs))
        return original_function(*args, **kwargs)
    return wrapper


def my_timer(original_function):

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_function(*args, **kwargs)
        end = time.time() - start
        print("Time Taken for {}() to Execution : {} Seconds".format(original_function.__name__, end))
        return result
    return wrapper


@my_timer
@my_logger
def display_info(*args, **kwargs):
    time.sleep(1)
    print("Input Arguments : {}".format(args))
    print("Input Keyword Arguments : {}".format(kwargs))


display_info("Ganesh", "Manal", address="Aurangabad")
