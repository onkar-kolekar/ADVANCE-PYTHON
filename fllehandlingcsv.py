"""
import csv
with open('firstfile.csv','r') as fp:
    r=csv.reader(fp)
    print(list(r))
"""
########################################################################################################################
import csv
with open('firstfile.csv','a+',newline='') as fp:
    w=csv.writer(fp)
    w.writerow(['name','age','salary'])
    for i in range(2):
        name=input('enter name::')
        age = int(input('enter age::'))
        sal = int(input('enter salary::'))
        fp.seek(0)
        r=csv.reader(fp)
    print(list(r))

#######################################################################################################################




























