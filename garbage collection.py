import gc
class Trial:
    def __init__(self):
        a=10
        b=20
        c=30
        d=a+b+c
        print(d)
    def __del__(self):
        print('Object destructed')
t1=Trial()
t2=Trial()
t1=10
t2=20