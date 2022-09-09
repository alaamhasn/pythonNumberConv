import sys

outNumber = '0'


def check_binary(binary):
    b = {'0', '1'}
    t = set(binary[2:])
    if b == t or t == {'0'} or t == {'1'}:
        return True
    else:
        return False


def check_octal(octal):
    try:
        int(octal, 8)
        return True
    except:
        return False


def check_decimal(decimal):
    if decimal.isdecimal():
        return True
    else:
        return False


def check_hex(hex):
    try:
        int(hex, 16)
        return True
    except ValueError:
        return False

#             0    1    2    3
typesList = ['B', 'O', 'D', 'H']

inNum = input("Enter The Number: ")
inNumType = input('Enter Number Type (B, O, D, H): ')
if inNumType not in typesList:
    print("Invalid Input Number Type")
    sys.exit()
else:
    if inNumType == 'B':
        if not check_binary(inNum):
            print("Invalid Input Number Value")
            sys.exit()
    elif inNumType == 'O':
        if not check_octal(inNum):
            print("Invalid Input Number Value")
            sys.exit()
    elif inNumType == 'D':
        if not check_decimal(inNum):
            print("Invalid Input Number Value")
            sys.exit()
    else:
        if not check_hex(inNum):
            print("Invalid Input Number Value")
            sys.exit()

outNumType = input('Enter Convert Type (B, O, D, H): ')
if outNumType not in typesList:
    print("Invalid Output Number Type")
    sys.exit()

if outNumType == 'B':
    if inNumType == outNumType:
        outNumber = inNum
    elif inNumType == 'O':
        outNumber = bin(int(inNum, 8))
    elif inNumType == 'D':
        outNumber = bin(int(inNum)).replace("0b", "")
    else:
        # Hex
        scale = 16
        num_of_bits = 8
        outNumber = bin(int(inNum, scale))[2:].zfill(num_of_bits)

elif outNumType == 'O':
    if inNumType == outNumType:
        outNumber = inNum
    elif inNumType == 'B':
        outNumber = oct(int(inNum, 2))
    elif inNumType == 'D':
        outNumber = oct(int(inNum))
    else:
        # H
        outNumber = oct(int(inNum, 16))

elif outNumType == 'D':
    if inNumType == outNumType:
        outNumber = inNum
    elif inNumType == 'B':
        outNumber = int(inNum, 2)
    elif inNumType == 'O':
        outNumber = int(inNum, 8)
    else:
        # H
        outNumber = int(inNum, 16)

elif outNumType == 'H':
    if inNumType == outNumType:
        outNumber = inNum
    elif inNumType == 'B':
        outNumber = hex(int(inNum, 2))
    elif inNumType == 'O':
        outNumber = hex(int(inNum, 8))
    else:
        # D
        outNumber = hex(int(inNum))



print('Default Input: {0} Type: {1} Converted To: {2} Result: {3}'.format(inNum, inNumType, outNumType, outNumber))
