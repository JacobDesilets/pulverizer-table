import sys

def pulverizer(phi, e):
    print("phi\te\t|\tQ\tR\t|\tx1\ty1\tx2\ty2")
    print("===========================================================================")
    a = phi
    b = e
    q = a // b
    r = a % b
    x1 = 1
    x2 = 0
    y1 = 0
    y2 = 1
    print(f"{a}\t{b}\t|\t{q}\t{r}\t|\t{x1}\t{y1}\t{x2}\t{y2}")
    while (r != 0):
        a = b
        b = r

        oldx1 = x1
        oldy1 = y1
        oldx2 = x2
        oldy2 = y2
        
        x2 = oldx1 - (q * oldx2)
        y2 = oldy1 - (q * oldy2)

        x1 = oldx2
        y1 = oldy2

        q = a // b
        r = a % b
        
        print(f"{a}\t{b}\t|\t{q}\t{r}\t|\t{x1}\t{y1}\t{x2}\t{y2}")

pulverizer(int(sys.argv[1]), int(sys.argv[2]))