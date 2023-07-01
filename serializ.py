"""
Serialization- converts one language objec to another
serialization/pickling/marshelling means converting python dict -----> pickle,json,yaml object
deserialization/unpickling/unmarshelling means converting python pickle,json,yaml object -----> python dict

"""
########################################################## ################################################################

#1 ) Serialization with pickle
# 1-dict--> pickle -----------------------------------> dump()
# 2-pickle--> dict -----------------------------------> load()
from gettext import install

import pip

"""
# 1-dict--> pickle -----------------------------------> dump()
import pickle
my_python_dict={
    'name':'Onkar',
    'Age':25,
    'Salary': 25000,
    'Degree': 'MCA'
}
with open('pickeddata.pickle','wb') as fp:
    data=pickle.dump(my_python_dict,fp)
    print(data)

# 2-pickle--> dict -----------------------------------> load()

with open('pickeddata.pickle','rb') as fp:
    data1=pickle.load(fp)
    print(data1)
    """
###########################################################################################################################

# 2) Serialization with JSON
# dict--> JSON -------------------------------->
# 1- dump() --> dict to JSON and store in file
# 2- dumps() --> dict to JSON and store in string

# JSON--> dict ----------------------------------->
# 1- load() --> Read file and then JSON to dict
# 2- loads()--> JSON string to dict
"""

import json
my_dict={
    'name':'Onkar',
    'Age':25,
    'Salary': 25000,
    'Degree': 'MCA'
}
# dumps() --> dict to JSON and store in string

# dict--> JSON -------------------------------->
data2=json.dumps(my_dict)
print(data2)

# dump() --> dict to JSON and store in file

with open('sample.json','w') as fp:
    json.dump(my_dict,fp,indent=4)

# JSON--> dict ----------------------------------->
# 1- load() --> Read file and then JSON to dict

with open('sample.json','r') as fp:
    data=json.load(fp)
    print(data)

# 2- loads()--> JSON string to dict
json_str='''{
    "name": "Onkar",
    "Age": 25,
    "Salary": 25000,
    "Degree": "MCA"
}'''

'''data_st=json.loads(json_str)
print(data_st)'''


# Question-- Diff btn JSON and Python Dict
'''"""
#-----------------------------------------------------------------------------------------------------------------------
 #            JSON                                  |                                                 DICT
#-----------------------------------------------------------------------------------------------------------------------
#1   Everything in ""                               |                                     1 .        in ' ' and " "
#2   Number                                         |                                     2.         int, float
#3   json                                           |                                     3.         dict
#4   bool- true false                               |                                     4          bool- True False
#5   null                                           |                                     5          None
#-----------------------------------------------------------------------------------------------------------------------"""


################################################################################################################################################


#3) Serialization using YAML
# dict--> yaml -------------------------------->
# 1- dump() --> dict to yaml and store in file

# yaml---> dict
#safe_load()

#--------------------------------------------------------------------------------------
'''
from pyaml import yaml

my_dict={
    'name':'Onkar',
    'Age':25,
    'Salary': 25000,
    'Degree': 'MCA'
}
'''
# dict--> yaml -------------------------------->
# 1- dump() --> dict to yaml and store in file
'''
with open('test.yaml','w') as fp:
    yaml.dump(my_dict,fp)
'''
# yaml--> dict -------------------------------->
# safe_load()
'''
with open('test.yaml','r') as fp:
    data=yaml.safe_load(fp)
    print(data)
'''
##########################################################################################################################################












