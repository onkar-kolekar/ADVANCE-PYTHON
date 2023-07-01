'''class Profit_loss:
    company_name='TCS'                                                      #<--- Static/Class Variable
    def __init__(self,purchase_amt,sale_amt,qnty):
        self.purchased_amt=purchase_amt                                     #<---Instance Variable
        self.sales_amt=sale_amt                                             #<---Instance Variable
        self.quantity=qnty                                                  #<---Instance Variable
    def show(self):
        purchased_total=self.purchased_amt*self.quantity                    #<--- purchased_total  is a local variable
        sales_total=self.sales_amt*self.quantity                            #<--- sales_total  is a local variable
        profit=sales_total-purchased_total                                  #<--- profit  is a local variable
        if profit>0:
            print(f'{profit} profit made by {Profit_loss.company_name}')    #<--- Calling class level variable with class name
        else:
            print(f'{profit} loss made by {Profit_loss.company_name}')      #<--- Calling class level variable with class name
obj = Profit_loss(25000,3000,20)
obj.show()
'''

#########################################################################################################################################################

'''class Profit_loss:
    company_name='TCS'                                                      #<--- Static/Class Variable
    def __init__(self,purchase_amt,sale_amt,qnty):
        self.purchased_amt=purchase_amt                                     #<---Instance Variable
        self.sales_amt=sale_amt                                             #<---Instance Variable
        self.quantity=qnty                                                  #<---Instance Variable

    def calculas(self):
        purchased_total = self.purchased_amt * self.quantity
        sales_total = self.sales_amt * self.quantity
        self.profit = sales_total - purchased_total
        return self.profit
    def show(self):
        self.calculas()
        if self.profit>0:
            print(f'{self.profit} profit made by {Profit_loss.company_name}')    #<--- Calling class level variable with class name
        else:
            print(f'{self.profit} loss made by {Profit_loss.company_name}')      #<--- Calling class level variable with class name
obj = Profit_loss(25000,3000,20)
obj.show()'''

########################################################################################################################################################

'''class Area:
    pie=3.14
    def __init__(self,radius):
        self.rad=radius
    def area_show(self):
        area=(self.rad**2)*Area.pie
        print(area)
obj=Area(5)
obj.area_show()
'''
######################################################################################################################################################

class delete_element_from_list:
    list_range=int(input('Enter the range you want:'))
    def list_element(self):
        self.l1=[]
        for j in range(delete_element_from_list.list_range):
            i = int(input('enter no::'))
            self.l1.append(i)
        print(self.l1)
    def find_and_delete(self):
        self.list_element()
        i=int(input('Enter the number to Find in list and delete from the list::'))
        for j in self.l1:
            if j==i:
                self.l1.remove(j)
        print('The list after removing:',self.l1)
obj= delete_element_from_list()
obj.find_and_delete()




















