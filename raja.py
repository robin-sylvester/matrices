import os
import sys

def write_me_up(henny):
    matija = 1
    for i in range(henny):
        for j in range(henny):
            if j<i:
                sys.stdout.write("  ")
            else:
                if i==0:
                    sys.stdout.write(str(matija) + " ")
                    matija+=1
                else:
                    sys.stdout.write(str(matija))
                    matija+=1
        sys.stdout.write("\n")

