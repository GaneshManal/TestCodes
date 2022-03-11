# THis is the how it works.
'''
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function


def display():
    print "Ran Display Functionality"

decorated_display = decorator_function(display)
decorated_display()
'''


# This is how it is configured.
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function


@decorator_function
def display():
    print "Ran Display Functionality"


# 1 & 2 calls are similar
# 1
'''
decorated_display = decorator_function(display)
decorated_display()
'''

# 2
display()