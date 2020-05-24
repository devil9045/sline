import math


def lopol():
    print('''Length Of Perpendicular From A Point On A Line
Enter values in form listed below
(x1 , y1)
ax + by + c = 0''')

    x1 = float(input('x1: '))
    y1 = float(input('y1: '))
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))

    print(f'''
({x1} , {y1})
{a}x + {b}y + {c} = 0''')

    p = ((a * x1) + (b * y1) + c) / (math.hypot(a, b))

    print(abs(p))

