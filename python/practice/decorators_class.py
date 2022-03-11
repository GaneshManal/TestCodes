class DecoratorClass(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('Call executed this before : {}()'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display():
    print "Ran Display Functionality"


@DecoratorClass
def display_info(name, state):
    print('display_info ran with arguments name = {} and state = {}.'.format(name, state))


display_info('Ganesh', 'Maharashtra')
display()

