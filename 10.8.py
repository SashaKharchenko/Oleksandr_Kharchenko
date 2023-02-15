from math import gcd
error=0
def clear_error():
    global error
    error=0
def reduce(a):
    global error
    if type(a[0])==int and type(a[1])==int and a[1]>0:
        error=0
        c=gcd(a[0],a[1])
        d=a[0]/c
        e=a[1]/c
        return (int(d),int(e))
    error=1
    return (None,None)
def add(a,b):
    global error
    if type(a[0])==int and type(a[1])==int and a[1]>0 and b[1]>0 and type(b[0])==int and type(b[1])==int:
        error=0
        c=a[0]*b[1]+b[0]*a[1]
        d=a[1]*b[1]
        return reduce((c,d))
    error=1
    return (None,None)
def mul(a,b):
    global error
    if type(a[0])==int and type(a[1])==int and a[1]>0 and b[1]>0 and type(b[0])==int and type(b[1])==int:
        error=0
        c=a[0]*b[0]
        d=a[1]*b[1]
        return reduce((c,d))
    error=1
    return (None,None)
def sub(a,b):
    global error
    if type(a[0])==int and type(a[1])==int and a[1]>0 and b[1]>0 and type(b[0])==int and type(b[1])==int:
        error=0
        c=a[0]*b[1]-b[0]*a[1]
        d=a[1]*b[1]
        return reduce((c,d))
    error=1
    return (None,None)
def div(a,b):
    global error
    if type(a[0])==int and type(a[1])==int and a[1]>0 and b[1]>0 and type(b[0])==int and type(b[1])==int:
        error=0
        c=a[0]*b[1]
        d=a[1]*b[0]
        if d<0:
            c=-c
            d=-d
        return reduce((c,d))
    error=1
    return (None,None)
def create(m,n):
    return reduce((m,n))
def inp():
    return reduce((int(input("m=")),int(input("n="))))
def prt(a):
    global error
    if type(a[0])==int and type(a[1])==int and a[1]>0:
        error=0
        print(a[0],"/",a[1])
    else:
        error=1
        print(None,"/",None)
def eq(a,b):
    global error
    if type(a[0])==int and type(a[1])==int and a[1]>0 and b[1]>0 and type(b[0])==int and type(b[1])==int:
        error=0
        if a[0]*b[1]==a[1]*b[0]:
            return True
        return False
    error=1
    return (None,None)
def lt(a,b):
    global error
    if type(a[0])==int and type(a[1])==int and a[1]>0 and b[1]>0 and type(b[0])==int and type(b[1])==int:
        error=0
        if a[0]*b[1]<a[1]*b[0]:
            return True
        return False
    error=1
    return (None,None)
if __name__=="__main__":
    k=int(input("k="))
    s=(0,1)
    for i in range(k):
        a=inp()
        s=add(s,a)
    prt(s)
    prt(div((1,1),s))
        
