def trace(fun):
    count=0
    def _trace(*args, **kwargs):
        nonlocal count
        count+=1
        print(count,*args,**kwargs)
        res=fun(*args, **kwargs)
        count=0
        return res
    return _trace

@trace
def fact(n,s=1):
    if n==0:
        return s
    s*=n
    n-=1
    return fact(n,s)

@trace
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
if __name__=="__main__":
    a=fact(3)
    print("\n")
    a=fib(4)
