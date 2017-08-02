class Demo(object):

    def go(self, *gam, **ram):
        print 'Go: ', gam
        print 'Go: ', ram


obj = Demo()
obj.go(5, 10, a="ganesh", b="manal")

