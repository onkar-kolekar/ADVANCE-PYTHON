# Super method --> It is used to call parent method without overriding it even if names are same
'''
class personal_details:
    def __init__(self,name,age):
        self.name_of_person=name
        self.age_of_person=age
    def show(self):
        print(self.name_of_person)
        print(self.age_of_person)

class higher_details(personal_details):
    def __init__(self,name,age,marks,grade):
        super().__init__(name, age)                             <------------------ Super method call
        self.marks_obtain=marks
        self.grade=grade
    def show(self):
        super().show()                                          <------------------ Super method call
        print(self.marks_obtain)
        print(self.grade)

obj=higher_details('Onkar',25,86.5,'A')
obj.show()

'''

#################################################################################################################################################

#
# class A:
#     def m1(self):
#         print('in A')
# class C:
#     def m1(self):
#         print('In C')
# class B(C,A):
#     def m1(self):
#         super(B, self).m1()                                    # <------------------ Super method call
#         print('In B')
#
# obj2=B()
# obj2.m1()

#################################################################################################################################################




class m3:
    def __init__(self,bank_name,bank_branch):
        self.BnakName=bank_name
        self.Branch=bank_branch
    def show(self):
        print(self.Branch)
        print(self.BnakName)
class m2(m3):
    def __init__(self,bank_name,bank_branch,profit,turnover):
        super().__init__(bank_name,bank_branch)
        self.profit=profit
        self.turnover=turnover
    def show(self):
        super().show()
        print(self.profit)
        print(self.turnover)
obj =m2('HDFC','KM',1000,15000)
obj.show()











