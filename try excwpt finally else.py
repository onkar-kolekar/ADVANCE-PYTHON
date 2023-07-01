'''
Exception-> It is an event that occurs exceptionally

try:
    risky code
except:
    handling code
else:
    this code will execute only after the try block is executed successfully
finally:
    This code will execute always

Valid sequence to use-
1. try->except
2. try->finally
3. try->except->finally
4. try->except->else->finally

Invalid sequeces-
1. try->finally->except
2. try->else->finally
3.try->except->finally->else
'''

'''

class practice:
    def normal(self):
        try:
            a=int(input('Enter the 1st no:'))
            b=int(input('Enter the 2nd no:'))
            c=a/b
        except ZeroDivisionError as e:
            print('The Error is: ',e)
        except ValueError as e:
            print('The name Error is: ',e)
        else:
            print('The division is:',c)
        finally:
            print('The final close')

obj=practice()
obj.normal()

'''

#########################################################################################################################################

'''
class practice:
    def normal(self):
        try:
            a=int(input('Enter the 1st no:'))
            b=int(input('Enter the 2nd no:'))
            c=a/b
        except (ZeroDivisionError,ValueError):
            print('The Error is: ')

        else:
            print('The division is:',c)
        finally:
            print('The final close')

obj=practice()
obj.normal()

'''

#####################################################################################################################
'''
class practice:
    def normal(self):
        try:
            a=int(input('Enter the 1st no:'))
            b=int(input('Enter the 2nd no:'))
            c=a/b
        except:
            print('error')
        else:
            print('The division is:',c)
        finally:
            print('The final close',)
obj=practice()
obj.normal()
'''

########################################################################################################################
'''
try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print("Error Code:",e)
except ValueError as e:
    print('Error Code:',e)

'''
x = int(input());
for i in range(x):
    try:
        a, b = input().split()
        print(int(a)/int(b))
    except ZeroDivisionError as e:
        print("Error Code: ",e)
    except ValueError as v:
        print('Error Code:',v)















