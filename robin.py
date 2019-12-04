import os
import sys
from raja import write_me_up

#if __name__=="__main__":
#   main()

print('Choose your number: ')

raw = input()
henny = int(raw)

while henny > 10 or henny < 3:
    print('Oh honey, no honey')
    print('Choose again')
    raw = input()
    henny = int(raw)

write_me_up(henny)
