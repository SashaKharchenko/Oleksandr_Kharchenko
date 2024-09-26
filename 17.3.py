def dec3(fun):
    def _dec3(*args, **kwargs):
        if len(args)!=len(kwargs):
            raise Exception("number of args should be equal to number of kwargs")
        return fun(*args, **kwargs)
    return _dec3

@dec3
def func(*args,**kwargs):
    a=list(map(float,args))
    kw=list(map(float,kwargs.values()))
    p=1
    for i in range(len(a)):
        t=a[i]+1/kw[i]
        p*=t
    return p
if __name__=="__main__":
    print(func(1,2,3,y1=3,y2=2,y3=1))
    print(func(1,2,3,4,y1=3,y2=2,y3=1))
