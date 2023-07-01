import logging
import os

# logging.basicConfig(filename='logs.log',level=10,
#                     format='%(asctime)s - %(levelname)s - %(name)s -  %(message)s',
#                     datefmt='%d-%m-%Y %I:%M:%S')
# logger = logging.getLogger(os.path.basename(__file__))
# def bonuscal(sal):
#     try:
#         bonus = (sal / 100) * 5
#     except ValueError as e:
#         logger.critical(e)
#     return bonus
#
#
# def Personal_info():
#
#     logger.info("taking inputs from user")
#     try:
#
#         name = input("Enter the Name:")
#         age = int(input("Enter the Age:"))
#         sal = int(input("Enter the Sal:"))
#     except ValueError as e:
#         logger.critical(e)
#     else:
#         return name, age, sal
#     finally:
#         pass
#
#
# def GrossSalCal(s1, b1):
#     try:
#         gross_sal = s1 + b1
#     except Exception as e:
#         logger.exception(e)
#
#     return gross_sal
#
#
# # trigerring --
# def main():
#     logger.info("entering into main function")
#     print("Employee Bonus Cal Program")
#     logging.info("executing personal info")
#     n, a, s = Personal_info()
#     logger.info("salary of emplyee {} is {}".format(n,s))
#     logger.info("calculating bonus")
#     b = bonuscal(s)
#     logger.info("calculating gross salary")
#     gross_sal = GrossSalCal(s, b)
#     print("Name is :", n)
#     print("Age is:", a)
#     print("Sal is:", s)
#     print("Bonus is :", b)
#     print("Gross Sal is :", gross_sal)
#
# if __name__=='__main__':
#     main()
#

##########################################################################################
#
# logging.basicConfig(filename='vlog.log', filemode='a', level=20,
#                     format=('%(asctime)s-%(message)s-%(name)s-%(levelname)s,%(lineno)d'),
#                     datefmt='%d-%m-%Y %I%M%S')
# logger = logging.getLogger(os.path.basename(__file__))
#
#
# class myClass:
#     @staticmethod
#     def saple(a,b):
#         try:
#             logger.info('taking two values')
#             ax = a
#             bx = b
#             c = ax + bx
#         except Exception as e:
#             logger.exception('something went wrong')
#         else:
#             logger.info('printing addition')
#             print(c)
#
#
# obj = myClass()
# obj.saple(10, 20)
#

logging.basicConfig(filename='vlog.log',filemode='a',level=10,
                    format=('%(asctime)s-%(pathname)s-%(module)s-%(funcName)s-%(message)s-%(levelname)s-%(lineno)d'),
                    datefmt=('%d/%m/%Y %I:%M:%S:%ms'))
logger=logging.getLogger(os.path.basename(__file__))

def mydef(a,b):
    try:
        logger.info('assign argument')
        ax=a
        bx=b
        c=ax/bx
    except ZeroDivisionError as e:
        logger.error(e)
    else:
        logger.info('printing output')
        print(c)
mydef(10,0)