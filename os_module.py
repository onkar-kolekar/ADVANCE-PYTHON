import os
print(os.getcwd())                                                      #get curent working directory
os.chdir(r"C:\Users\Onkar Kolekar\OneDrive\Desktop\changeddirectory")   #change current working directory
print(os.getcwd())
#os.mkdir('k4')                                                         #make single directories
#os.makedirs(r'k1/k2/k3')                                               #make multiple directories
# os.rmdir(r'k1/k2/k3')                                                 #remove single directory
# os.removedirs(r'k1/k2/k3')                                            #remove multiple directories

with open(r'k1/k2/k3/test.txt','w+') as fp:
    fp.write('Hi')
    fp.seek(0)
    data=fp.read()
    print(data)

os.remove(r'k1/k2/k3/test.txt')                                         #remove single file

print(os.path.isdir(r'k1/k2/k3'))                                       #return bool if directory present at given path
print(os.path.isfile('test.txt'))                                       #return bool if file present at given path

print(os.listdir(r'k1/k2'))                                             # return list of directories in current given location
print(os.listdir(r'.'))                                                 # return list of all directories in current given location
os.chdir(r"C:\Users\Onkar Kolekar\PycharmProjects\AdvancePython")
filedata=os.listdir(r'.')
for i in filedata:
    if i.endswith('.py'):
        print(i)


# For restart your system :
os.system(r'shutdown/r/t1')

# For Logout your system :
os.system('shutdown -l')
