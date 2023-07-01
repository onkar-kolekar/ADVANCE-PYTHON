"""'fp = open("test.txt",'r')
read_data=fp.read()
print(read_data)

###################################################################################################################

fp = open("test.txt",'r')
read_lines=fp.readlines()
print(read_lines)

####################################################################################################################

fp = open("test.txt",'r')
read_n=fp.read(5)
print(read_n)

###################################################################################################################

fp = open("test.txt",'r')
read_line=fp.readline()
print(read_line)


###################################################################################################################

fp=open('test.txt')
print(fp.readline(),end='')
print(fp.readline())

"""

####################################################################################################################

'''with open('test.txt','a') as fp:
    data=fp.write('\nHello sanket')'''
#############################################################################################################
'''

Combinaions-
r+-> read then write    <---------------------------(file should be present at given location)
w+-> write then read(override) <---------------------------(If file not found i will crate new file)
a+-> write then read(append) <---------------------------(If file not found i will crate new file)

'''
#########################################################################################################

'''with open("test123.txt",'r+') as fp:
    data=fp.read()
    print(data)
    data1=fp.write('New content1')
    fp.seek(0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    print(fp.read())'''
#########################################################################################################
"""
with open('focus.txt','w+') as focus:
    focus.writelines(['1.line1','\n2.line2'])
    focus.seek(0)
    print(focus.readlines())
    focus.close()"""
#############################################################################################################
"""
with open('focus.txt','a+',newline='') as fp:
    fp.writelines(['\n3.Line3','\n4.Line4'])
    fp.seek(0)
    print(fp.read())
"""
#############################################################################################################
"""
with open('focus.txt','a+',newline='') as fp:
    fp.write('hxg')
    print(fp.writable())
    fp.close()
    print(fp.closed)
"""
##############################################################################################################
'''
with open('focus.txt','x') as fp:                 #FileExistsError: [Errno 17] File exists: 'focus.txt'
    fp.write('Hello')
'''
##############################################################################################################
'''
with open('focus1.txt','x') as fp:
    fp.write('hello')
'''
##############################################################################################################





































