'''class Emp:
    def __init__(self,a,b):
        print('I started with Advance Python')
        self.num1=a
        self.num2=b
    def addition(self):
        print("The addition of two given numbers is::",self.num1+self.num2)
    def subtraction(self):
        print('The substraction of two given numbers is::',self.num1-self.num2)

obj = Emp((int(input('Enter the first No.'))),(int(input('Enter the Second No.'))))
obj.addition()
obj.subtraction()'''

#######################################################################################################################

'''class practice:
    def __init__(self,list1,list2):
        #print(id(self))
        self.l1=list1
        self.l2=list2
    def listitems(self):
        for i in self.l1:
            self.l2.insert(0,i)
        print('The Reversed list::',self.l2)

obj=practice([10,20,24,20,121,10,14,24,57,585,9,6,5],[])
#print('the id',id(obj))
#print("list1",obj.a)
#print("list2",obj.b)
obj.listitems()'''

#######################################################################################################################

'''class prime_no:
    def __init__(self,a):
        self.num=a
    def execution(self):
        for i in range(2,self.num):
            flag = True
            for j in range(2,i):
                if i%j==0:
                    flag=False
            if flag:
                print(i)

obj= prime_no(100)
obj.execution()'''

########################################################################################################################

'''class char_vowel_consonent:
    def str_find(self):
        str1=input('Enter the strig::')
        cons_count=0
        vowel_count=0
        for i in str1:
            if (i>='A' and i<='Z') or (i>='a' and i<='z'):
                if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                    vowel_count+=1
                else:
                    cons_count+=1
        print("Vowel count::",vowel_count)
        print("Consonent count::",cons_count)

obj=char_vowel_consonent()
obj.str_find()'''

#######################################################################################################################

'''a=38
for i in range(2,a):
    flag=True
    for j in range(2,i):
        if i%j==0:
            flag=False
    if flag:
        print(f'The number {i} is prime')
    else:
        print(f'The number {i} is not prime')'''

#######################################################################################################################













