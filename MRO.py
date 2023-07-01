'''class d:
    def m1(self):
        print('in m1 of d')

class e:
    def m1(self):
        print('in m1 of e')

class f:
    def m1(self):
        print('in m1 of f')

class b(d,e):
    def m1(self):
        print('in m1 of b')

class c(d,f):
    def m1(self):
        print('in m1 of c')

class a(b,c):
    def m1(self):
        print('in m1 of a')
print(a.mro())
'''
#################################################################################

'''class a:
    def m1(self):
        print('in m1 of a')

class b:
    def m1(self):
        print('in m1 of b')

class c(a,b):
    def m1(self):
        print('in m1 of c')

class d(c,b):
    def m1(self):
        print('in m1 of d')
print(d.mro())
'''

#################################################################################\
'''
class a:
    def m1(self):
        pass

class b:
    def m1(self):
        pass

class c:
    def m1(self):
        pass

class d:
    def m1(self):
        pass

class e():
    def m1(self):
        pass

class k1(c,a,b):
    def m1(self):
        pass

class k2(b,d,e):
    def m1(self):
        pass

class k3(a,d):
    def m1(self):
        pass

class z(k1,k3,k2):
    def m1(self):
        pass
                                                                                           
print(z.mro())'''

#################################################################################\
'''
class o:
    def m1(self):
        pass

class a(o):
    def m1(self):
        pass

class b(o):
    def m1(self):
        pass

class c(o):
    def m1(self):
        pass

class d(o):
    def m1(self):
        pass

class e(o):
    def m1(self):
        pass

class k1(a,b,c):
    def m1(self):
        pass

class k2(b,d):
    def m1(self):
        pass

class k3(c,d,e):
    def m1(self):
        pass

class z(k1,k2,k3):
    def m1(self):
        pass

class o:
    def m1(self):
        pass
print(z.mro())'''

#######################################################################################################################################

class a:
    def m1(self):
        pass

class b(a):
    def m1(self):
        pass

class c(a):
    def m1(self):
        pass

class d(a):
    def m1(self):
        pass

class e(c):
    def m1(self):
        pass

class f(c):
    def m1(self):
        pass

class g(c):
    def m1(self):
        pass

class h(e,f,g):
    def m1(self):
        pass
print(h.mro())