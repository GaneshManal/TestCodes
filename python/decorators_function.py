def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print "Ran Display Functionality"


@decorator_function
def display_info(name, state):
    print('display_info ran with arguments name = {} and state = {}.'.format(name, state))


display()
display_info('Ganesh', 'Maharashtra')
