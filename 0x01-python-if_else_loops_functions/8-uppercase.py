#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False


def uppercase(str):
    result = ""
    for c in str:
        if (islower(c)):
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{:c}".format(result))
