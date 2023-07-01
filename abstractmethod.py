from abc import ABC,abstractmethod

class example(ABC):
    @abstractmethod
    def m1(self):
        pass

class exp2(example):
    def m1(self):
        print('in imp m1')
obj=exp2()
obj.m1()




