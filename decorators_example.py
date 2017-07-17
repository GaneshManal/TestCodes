import logging
import time


def my_logger(original_function):
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)
        logging.info('Function called with arguments args {}, kwargs {}'.format(args, kwargs))
        return original_function(*args, **kwargs)
    return wrapper


def my_timer(original_function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_function(*args, **kwargs)
        end = time.time() - start
        print("Time Taken for {}() to Execution : {} Seconds".format(original_function.__name__, end))
        return result
    return wrapper


@my_logger
@my_timer
def display_info(*args, **kwargs):
    time.sleep(1)
    print("Input Arguments : {}".format(args))
    print("Input Keyword Arguments : {}".format(kwargs))


display_info("Ganesh", "Manal", address="Aurangabad")
