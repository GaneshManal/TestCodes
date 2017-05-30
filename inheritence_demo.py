class A(object):
    def go(self):
        print 'inside A'
        print "Go - A"


class B(A):
    def go(self):
        print 'inside B'
        super(B, self).go()
        print "Go - B"


class C(A):
    def go(self):
        print 'inside C'
        super(C, self).go()
        print "Go - C"


class D(B, C):
    pass
    '''
    def go(self):
        # super(D, self).go()
        print "Go - D"
    '''

a, b, c, d = A(), B(), C(), D()

'''
a.go()
print '-'* 50

b.go()
print '-'* 50

c.go()
print '-'* 50
'''

d.go()
print '-'* 50