import math


def eoboa():
    print('''Equation of angle bisector between two lines
Enter values in form listed below
(x1 , y1)
ax + by + c = 0''')

    a1 = float(input('a1: '))
    b1 = float(input('b1: '))
    c1 = float(input('c1: '))
    a2 = float(input('a2: '))
    b2 = float(input('b2: '))
    c2 = float(input('c2: '))

    print(f'''
{a1}x + {b1}y + {c1} = 0
{a2}x + {b2}y + {c2} = 0''')

    p = math.hypot(a1, b1)
    q = math.hypot(a2, b2)

    if (c1 >= 0 and c2) or (c1 <= 0 and c2 <= 0) >= 0:
        a3 = (a1 * q) - (a2 * p)
        b3 = (b1 * q) - (b2 * p)
        c3 = (c1 * q) - (c2 * p)

        a4 = (a1 * q) + (a2 * p)
        b4 = (b1 * q) + (b2 * p)
        c4 = (c1 * q) + (c2 * p)

        w = (a1 * a2) + (b1 * b2)

        if w < 0:
            print(f'''ANS:
LINE CONTAINING ACUTE ANGLE ==> {a3}x + {b3}y + {c3} = 0
LINE CONTAINING OBTUSE ANGLE ==> {a4}x + {b4}y + {c4} = 0
LINE CONTAINING ORIGIN ==> {a3}x + {b3}y + {c3} = 0
LINE NOT CONTAINING ORIGIN ==> {a4}x + {b4}y + {c4} = 0''')

        if w > 0:
            print(f'''ANS:
LINE CONTAINING OBTUSE ANGLE ==> {a3}x + {b3}y + {c3} = 0
LINE CONTAINING ACUTE ANGLE ==> {a4}x + {b4}y + {c4} = 0
LINE CONTAINING ORIGIN ==> {a3}x + {b3}y + {c3} = 0
LINE NOT CONTAINING ORIGIN ==> {a4}x + {b4}y + {c4} = 0''')

    if c1 <= 0 or c2 <= 0:
        a3 = (a1 * q) - (a2 * p)
        b3 = (b1 * q) - (b2 * p)
        c3 = (c1 * q) - (c2 * p)

        a4 = (a1 * q) + (a2 * p)
        b4 = (b1 * q) + (b2 * p)
        c4 = (c1 * q) + (c2 * p)

        w = (a1 * a2) + (b1 * b2)

        if w < 0:
            print(f'''ANS:
LINE CONTAINING OBTUSE ANGLE ==> {a3}x + {b3}y + {c3} = 0
LINE CONTAINING ACUTE ANGLE ==> {a4}x + {b4}y + {c4} = 0
LINE NOT CONTAINING ORIGIN ==> {a3}x + {b3}y + {c3} = 0
LINE CONTAINING ORIGIN ==> {a4}x + {b4}y + {c4} = 0''')

        if w > 0:
            print(f'''ANS:
LINE CONTAINING ACUTE ANGLE ==> {a3}x + {b3}y + {c3} = 0
LINE CONTAINING OBTUSE ANGLE ==> {a4}x + {b4}y + {c4} = 0
LINE NOT CONTAINING ORIGIN ==> {a3}x + {b3}y + {c3} = 0
LINE CONTAINING ORIGIN ==> {a4}x + {b4}y + {c4} = 0''')