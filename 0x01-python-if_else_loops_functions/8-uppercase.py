#!/usr/bin/python3
def uppercase(str):
    converter = ''
    for letter in str:
        iterator = ord(str)
        if (iterator >= 97) and (iterator <= 122):
            converter += chr(iterator - 32)
        elif (iterator >= 65) and (iterator <= 90):
            converter += chr(iterator)
        else:
            converter += chr(iterator)
    print("{}".format(iterator))
