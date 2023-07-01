# What is Python Logging?
# How logging is used in Python?
# How do you create a logging level in Python?
# What is the importance of logging in Python?
# What are the Python logging best practices?

import logging

logging.basicConfig(filename='Log.txt',level=10,filemode='w',
                    format='%(asctime)s-%(levelname)s-%(message)s')  # datefmt='%Y-%m-%d,%H:%M:%S.%f')


logging.critical('Critical')
logging.error('Error')
logging.warning('Warning')
logging.info('Information')
logging.debug('Debug')

def beautiparlour(girl):
    logging.info('Decorator called')
    def select_pkg():
        print('I am going to parlour')
        girl()
        print('I am done with makeup, Thank you')
    return select_pkg

@beautiparlour
def normal_girl():
    logging.info('Decorator created')
    print('I am a normal girl and I am doing makeup now _-_')



#----------------------------------------------------------------------------------

import logging
import os
logging.basicConfig(filename='log.txt',filemode='w',
                    datefmt='%d-%m-%y-%I-%M-%S.%ms',level=10,format='%(asctime)s-%(levelname)s-%(lineno)d-%(pathname)s-%(funcName)s-%(name)s-%(message)s')
logger=logging.getLogger(os.path.basename(__file__))

def division(a,b):
    try:
        logger.info("Numbers assigned to num1 and num2")
        num1=a
        num2=b
        logger.info("Doing division")
        divv=num1/num2
        print(divv)
    except ZeroDivisionError as e:
        logger.error(e)
    else:
        logger.info("returning addd")
        return divv
    finally:
        logger.info("Terminated")
division(20,10)












