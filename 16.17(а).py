import math
def term(x,eps=0.0001):
    assert abs(x)<1, "x>=1"
    assert eps>0, "eps<=0"
    t=x
    k=1
    while abs(t)>eps:
        yield t
        k+=1
        t=-t*x*(k-1)/k
def ln(x,eps=0.0001):
    assert abs(x)<1, "x>=1"
    assert eps>0, "eps<=0"
    s=0
    for t in term(x,eps):
        s+=t
        yield s
if __name__=="__main__":
    sums=ln(-0.5)
    for a in sums:
        print(a)
    
