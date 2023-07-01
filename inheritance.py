#    1. Single Level Inheritnce
'''
class grandparent:
    def grandparent_method(self):
        print('In Grandparents class')
class parents(grandparent):
    def parents_method(self):
        print('In parent class')

obj=parents()
obj.parents_method()
obj.grandparent_method()
 '''
##############################################################################################################################################

#    2. Multi Level Inheritnce
'''
class level1:
    def level1_method(self):
        print('In Level 1 class')

class level2(level1):
    def level2_method(self):
        print('In level 2 class')

class level3(level2):
    def level3_method(self):
        print('In level 3 class')

class level4(level3):
    def level4_method(self):
        print('In level 4 class')

obj=level4()
obj.level1_method()
obj.level2_method()
obj.level3_method()
obj.level4_method()
'''

'''
class PerDetails:
    def m1(self):
        print("Name")
        print("Age")

class AddPerDetails(PerDetails):
    def m2(self):
        print("Pan")
        print("Aadhar")

class CityPerDetails(AddPerDetails):
    def m3(self):
        print("City")

class EmailPerDetails(CityPerDetails):
    def m4(self):
        print("Email")

obj = EmailPerDetails()
obj.m1()
obj.m2()
obj.m4()
obj.m3()
'''

##############################################################################################################################################

#    3. Multiple Inheritnce
'''
class father:
    def father_method(self):
        print('Fathers empire')

class mother:
    def mother_method(self):
        print("Mother's empire")

class son(father,mother):
    def son_method(self):
        print("son's empire")

obj=son()
obj.son_method()
obj.father_method()
obj.mother_method()
'''

'''
class PerDetails:
    def m1(self):
        print("Name")
        print("Age")

class AddPerDetails:
    def m2(self):
        print("Pan")
        print("Aadhar")

class CityPerDetails(PerDetails,AddPerDetails):
    def m3(self):
        print("City")


obj = CityPerDetails()
obj.m1()
obj.m2()
obj.m3()
'''

##############################################################################################################################################

#    4. Hierarchical Inheritnce
'''
class parent:
    def parent_method(self):
        print('In parent Method')


class son(parent):
    def son_method(self):
        print('In son Method')

class daughter(parent):
    def daughter_method(self):
        print('In daughter Method')

obj=son()
obj.son_method()
obj.parent_method()

obj1=daughter()
obj1.daughter_method()
obj1.parent_method()
'''

##############################################################################################################################################

#    5. Hybrid Inheritnce
'''
class level1:
    def level1_method(self):
        print('In Level 1 class')

class level2(level1):
    def level2_method(self):
        print('In level 2 class')

class level3(level2):
    def level3_method(self):
        print('In level 3 class')

class level4(level3):
    def level4_method(self):
        print('In level 4 class')

class level5(level3):
    def level5_method(self):
        print('In level 5 class')
obj=level4()
obj.level1_method()
obj.level2_method()
obj.level3_method()
obj.level4_method()

obj1=level5()
obj1.level1_method()
obj1.level2_method()
obj1.level3_method()
obj1.level5_method()

'''



































