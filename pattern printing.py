for row in range(5):
    for col in range(5,row,-1):
        print('*', end=' ')
    print()
for row in range(6):
    for col in range(row):
        print('*',end=" ")
    print()


for row in range(8):
    for col in range(8):
        if row in (0,4) and col in (3,4):
            print('*',end=" ")
        elif row in(1,4) and col in (2,5):
            print('*', end=" ")
    print()
print()