import math


def popwrl():
    print('''Position of point w.r.t line
Enter values in form listed below
(x1 , y1)
ax + by + c = 0''')

    x1 = float(input('x1: '))
    y1 = float(input('y1: '))
    x2 = float(input('x2: '))
    y2 = float(input('y2: '))
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))

    print(f'''
({x1} , {y1})
{a}x + {b}y + {c} = 0''')

    p = (a * x1) + (b * y1) + c
    q = (a * x2) + (b * y2) + c

    if (p * q) < 0:
        print('BOTH POINTS LIES ON OPP SIDE OF LINE')

    elif (p * q) > 0:
        print('BOTH POINTS LIES ON SAME SIDE OF LINE')

    elif (p * q) == 0:
        print('ANY ONE POINT LIES ON THE LINE')
