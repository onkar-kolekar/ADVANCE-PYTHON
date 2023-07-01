'''fp=open('mail.txt')
mail_data=fp.read()
print(mail_data.format('Onkar','Feb-2023','DCC Sangli Home Loan'))

####################################################################################################

fp=open('mail.txt')
data=fp.readlines()
list1=[]
for mail in data:
    mail_id=mail.split(',')[1]
    list1.append(mail_id+' ')

fp = open('writedataofmail.txt', 'w')
fp.writelines(list1)
#####################################################################################################

fp=open('mail.txt')
data=fp.readlines()
l1=[]
for date in data:
    dob=date.split(',')[-1]
    l1.append(dob+'\n')

fp=open('dob.txt','w')
dob_data=fp.writelines(l1)

######################################################################################################

fp = open('test123.txt','r')
data= fp.readlines()
email_id = []
for line in data:
    word = line.split(',')
    for email in word:
        if '@' in email and email.split('@')[-1] in ['gmail.com','yahoo.com','rediffmail.com']:
            email_id.append(email+'\n')
fp1 = open('email_id_by_demand.txt','w')
fp1.writelines(email_id)
print("email id successfully written")

'''
















