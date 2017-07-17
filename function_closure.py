# Decorators


'''
def outer_function(msg):
    message = msg

    def inner_function():
        # Message is a free variable
        print message

    return inner_function
'''


# These are called as function closures.
def outer_function(message):
    def inner_function():
        # Message is a free variable
        print message

    # This function is waiting to be executed.
    return inner_function

hi_func = outer_function("Hi")
bye_func = outer_function("Bye")

hi_func()
bye_func()
