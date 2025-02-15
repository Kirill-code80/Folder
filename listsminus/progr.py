from math import pi,pow
def minus_plus(m):
    try:
        r=[]
        d=int(input())
    except ValueError:
        print('Only int')
    else:
        for i in range(d):
            f=int(input())
            if f > 1:
                f=1
                r.append(f)
            elif f < 1:
                f=-1
                r.append(f)
            else:
                f=0
                r.append(f)
            
    return r
