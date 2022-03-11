class Test:
    def __init__(self, test):
        print test.name


class xyz:
    def __init__(self):
        self.name = "Ganesh"


x_obj = xyz()
test_obj = Test(x_obj)
