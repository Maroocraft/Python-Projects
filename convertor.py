import time

print('Welcome to the convertor')
time.sleep(2)
chose = input('Length or weight? ')
if chose.lower() == "length" :
    print('Okay')
    len = input('(M)eter to (F)oot, (M)eter to (C)enimeter, (F)oot to (I)nch, (C)enimeter to (i)nch ')
    if len.lower() == 'm to f':
        print('Okay')
        meter = float(input('Enter meter: '))
        foot = meter * 3.28084
        print(f'{meter} meter is {foot} foot')
    elif len.lower() == "m to c":
        print('Okay')
        meter = float(input('Enter meter: '))
        centimeter = meter * 100
        print(f'{meter} meter is {centimeter} centimeter')
    elif len.lower() == "f to i":
        print('Okay')
        foot = float(input('Enter foot: '))
        inch = foot * 12
        print(f'{foot} foot is {inch} inch')
    elif len.lower() == "c to i":
        print('Okay')
        centimeter = float(input('Enter centimeter: '))
        inch = centimeter / 2.54
        print(f'{centimeter} centimeter is {inch} inch')
    else:
        print("Invalid input")
if chose.lower() == "weight":
    print('Okay')
    weight = input('(K)ilogram to (P)ound, (P)ound to (K)ilogram, (K)ilogram to (G)ram, (G)ram to (K)ilogram, ()')
    if weight.lower() == "k to p":
        print('Okay')
        kilogram = float(input('Enter kilogram: '))
        pound = kilogram * 2.20462
        print(f'{kilogram} kilogram is {pound} pound')
