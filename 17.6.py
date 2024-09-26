def dec6(fun):
    def _dec6(*args, **kwargs):
        if kwargs:
            raise Exception("function cannot have kwargs")
        return fun(*args, **kwargs)
    return _dec6

@dec6
def func(*args,**kwargs):
    lst=list(args)+list(kwargs.values())
    s=0
    for x in lst:
        s+=x
    if max(lst)>s:
        return 1
    else:
        return s
if __name__=="__main__":
    print(func(1,3,5))
    print(func(3,2,-1,-3))
    print(func(3,2,-1,k=-3))
