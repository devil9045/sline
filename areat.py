def areat():
    print('''AREA OF TRIANGLE FORMED BY THREE POINTS
Enter values in form listed below
(x1 , y1)
(x2 , y2)
(x3 , y3)''')

    x1 = float(input('x1: '))
    y1 = float(input('y1: '))
    x2 = float(input('x2: '))
    y2 = float(input('y2: '))
    x3 = float(input('x3: '))
    y3 = float(input('y3: '))

    print(f'''
({x1} , {y1})
({x2} , {y2})
({x3} , {y3})''')

    ans = ((x1 * y1) - (x2 * y1) + (x2 * y3) - (x3 * y2) + (x3 * y1) - (x1 * y3)) / 2
    if ans != 0:
        print(f'''
Ans = {abs(ans)}''')
    if ans == 0:
        print('POINTS ARE COLLINEAR')
