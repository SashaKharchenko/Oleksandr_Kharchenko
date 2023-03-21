def log1(x,eps):
    assert eps>0, "eps should be positive"
    assert abs(x)<1, "|x| should be <1"
    y=0
    t=x
    i=1
    while abs(t)>eps:
        y+=t
        t=t*(-x)*i/(i+1)
        i+=1
    return y
if __name__=="__main__":
    y=log1(0.5,0.0001)
    print(y)
    y=log1(2,0.01)
    print(y)
