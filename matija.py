import os
import sys

print('Choose your number: ')

raw = input()
henny = int(raw)

while henny > 10 or henny < 3:
    print('Oh honey, no honey')
    print('Choose again')
    raw = input()
    henny = int(raw)

#sum of first n numbers
matija = int(henny*(henny+1)/2)
matija = 1

'''
for i in range(henny):
    for j in range(henny):
        if j<i:
            print (' ', end = '')
        else:
            print (matija, end = '')
            matija+=1
    print ('\n')
'''

'''
for i in range(henny):
    for j in range(henny):
        if j<i:
            print ('  ', end = '')
        else:
            if i==0:
                print (matija, end = ' ')
                matija+=1
            else:
                print (matija, end = '')
                matija+=1
    print ('\n')
'''

'''
#sys.stdout.write("Hello World!")
for i in range(henny):
    for j in range(henny):
        if j<i:
            print ('  ', end = '')
        else:
            if i==0:
                sys.stdout.write(str(matija) + " ")
                matija+=1
            else:
                sys.stdout.write(str(matija))
                matija+=1
    sys.stdout.write("\n")
'''
