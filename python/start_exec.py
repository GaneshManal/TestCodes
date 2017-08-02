# Is this file been directly run by Python or being imported
if __name__ == "__main__":
    print "Ran Directly - Hence, module name : {}.".format(__name__)
else:
    print "Imported and executed - Hence, module name : {}.".format(__name__)

