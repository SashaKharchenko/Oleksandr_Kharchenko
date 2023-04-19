def trace(func_f):
    def _trace(*args, **kwargs):
        print(f"Name of function:{func_f.__name__}")
        for x in args:
            print(x)
        for key, value in kwargs.items():
            print(value)
        y=func_f(*args,**kwargs)
        print(y)
        return y
    return _trace
def ClassTracing(cls):
    for name, atr in cls.__dict__.items():
        if not name.startswith("__") and callable(atr):
            setattr(cls,name,trace(atr))
    return cls
            
@ClassTracing    
class Func:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def fact(self,n):
        if n<=1:
            return 1
        else:
            return n*self.fact(n-1)
    def cons(self,const):
        return const
if __name__=="__main__":
    a=Func(1,2,3)
    a.fact(5)
    a.cons(3)
