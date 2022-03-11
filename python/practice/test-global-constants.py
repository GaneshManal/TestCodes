ABCD = 123

def test():
    print("test: constant ABCD = {}".format(ABCD))

if __name__ == "__main__":
    print("main: constant ABCD = {}".format(ABCD))
    ABCD = 456
    test()

