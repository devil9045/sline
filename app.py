import math
import areat
import lopol
import popwrl
import eoboa


p = int(input('''STRAIGHT LINE FORMULAS BY HENISH
PRESS 1 FOR FINDING AREA OF TRIANGLE
PRESS 2 FOR FINDING LENGTH OF PERPENDICULAR FROM A POINT
PRESS 3 FOR FINDING POSITION OF POINTS  W.R.T. LINE
PRESS 4 FOR FINDING EQUATION OF BISECTOR OF LINES
-->'''))

if p == 1:
    areat.areat()

elif p == 2:
    lopol.lopol()

elif p == 3:
    popwrl.popwrl()

elif p == 4:
    eoboa.eoboa()

else:
    print("ENTER VALID VALUE")