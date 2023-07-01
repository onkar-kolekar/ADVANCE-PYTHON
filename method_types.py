class loan:
    bank_name='HDFC'
    def __init__(self,principle_amt, roi,tenure):                           #<--------------constructor
        self.principle_amt=principle_amt
        self.interest_rate=roi
        self.tenure=tenure
    def calculate_loan(self):                                               #<--------------instance method
        interest=(self.principle_amt*self.interest_rate*self.tenure)/100
        final_amt_with_interest=interest+self.principle_amt
        print("Bank Name:",loan.bank_name)
        print('Total {} Interest for {} years for {} Amount'.format(interest,self.tenure,self.principle_amt))
        print(f"Final Amount with Interest is {final_amt_with_interest}")

obj=loan(int(input()),int(input()),int(input()))
obj.calculate_loan()

######################################################################################################################################################
'''
class DataProcess:
    url = 'https://api.sampleapis.com/codingresources/codingResources'
    def __init__(self):
        self.username='admin'
        self.password = 'admin@123'
        self.host='192.168.1.27'
        self.port = 3606
    def connection(self):
        print("db connecting... with {}".format(self.username))
    def data_process(self):
        print("Data Processing")
    def data_dump(self):
        print("data dumped for {}".format(self.username))
    @classmethod                                                                    #<--------------inbuilt  method
    def test(cls):                                                                  #<--------------class method
        print(cls.url)

obj = DataProcess()
obj.connection()
obj.data_process()
obj.data_dump()
DataProcess.test()                                                                  #<--------------Calling class method
obj.test()                                                                          #<--------------Calling class method
'''
##################################################################################################################################################

# Another way to define class method
'''class Example:
    age = 55
    def Age_of_class_var(cls):
        print('\nThe age is:', cls.age)
# create printAge class method
Example.Age_of_class_var = classmethod(Example.Age_of_class_var)                    #----------------- Another way to define class method
Example.Age_of_class_var()'''

###################################################################################################################################################

'''class student_details:
    student_name='Onkar'
    student_std='8th'
    school_name='SBVA'
    Result='Pass'
    @classmethod
    def student_details(cls):
        print('\n',cls.student_name)
        print(cls.school_name)
        print(cls.student_std)
        print(cls.Result)
obj =student_details()
obj.student_details()'''

####################################################################################################################################################

'''class emp:
    @staticmethod                                                                   #<------------ inbuilt decorator for static method
    def calculatons(a,b,c):                                                         #<--------------static method
        result = a+b+c
        print(result)
ob1=emp()
ob1.calculatons(10,20,30)                                                           #<--------------calling static method with object
emp.calculatons(40,50,60) '''                                                          #<--------------calling static method with class name











