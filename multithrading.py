# 1. Creating Thread without using any class(Function base)

import threading
def func():
    for i in range(1, 11):
        qube = i ** 3
        print(qube)

t1 = threading.Thread(target=func)
t1.start()
t1.join()
print('main ttheard')
print('main ttheard')
print('main ttheard')
print('main ttheard')
print('main ttheard')
print('main ttheard')
print('main ttheard')

###############################################################################################################################################

# 2. Creating Thread by extending Thread Class

"""
from threading import Thread

class func(Thread):
    def run(self):                          <------------------ run() is a inbuilt method. Only run method can be written in this type of threading
        for i in range(10):
            print(i*2)
obj=func()
obj.start()
obj.join()
for i in range(10):
    print("In MainThread",i * 2)

"""
#############################################################################################################################################

# 3. Without extending thread class (Class base)
#
# from threading import Thread
# class func:
#     def example(self):
#         for i in range(10):
#             print(i*2)
# obj=func()
# t1=Thread(target=obj.example())
# t1.start()
# t1.join()
# for i in range(50):
#     print("In MainThread",i * 2)
#
#















