#!/usr/bin/python3
def islower(c):
    if ord('c') >= ord('a') and ord('c') <= ord('z'):
        return True
    else:
        return False

def uppercase(str):
    for c in str:
        if(c.islower()):
            print({":c"}.format(ord(c) - 32), end="")
    print("")