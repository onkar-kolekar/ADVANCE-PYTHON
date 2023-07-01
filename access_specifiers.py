'''
Mainly there are three types of specifiers
1 public -> accessible at all levels                                                                ex-   var=100
2 protected -> accessible with one child class only(not possible in python)                           ex-  _var=100
3 private -> accessible within class only(not possible in python)                                 ex-  __var=100

Name mangling -> Accessing private variable outside
'''

''''
class access_specifiers:
    t=100                  #<------------------------------------------ public variable
    print(t)
    _t1=200                #<------------------------------------------ protected variable
    print(_t1)
    __t3=300               #<------------------------------------------ private variable
    print(__t3)

obj=access_specifiers()
print(obj._access_specifier__t3)        #<------------------------------ Name Mangling

'''

class test:
    a=100
    _b=200
    __c=300
class test1(test):
    print(test.a)
    print(test._b)
obj=test1()
print(obj.__c)






