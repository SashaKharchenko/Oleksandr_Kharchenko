def dec4(fun):
    def _dec4(*args, **kwargs):
        for arg in args:
            if type(arg)!=str:
                raise Exception("type of args must be str")
        for kwarg in kwargs.values():
            if type(kwarg)!=str:
                raise Exception("type of kwargs must be str")   
        return fun(*args, **kwargs)
    return _dec4

@dec4
def func(*args,**kwargs):
    lst=list(args)+list(kwargs.values())
    new_lst=[]
    for s in lst:
        if s not in new_lst:
            new_lst.append(s)
    return new_lst
if __name__=="__main__":
    print(func("w","e","l",y1="3",y2="l",y3="1"))
    print(func(1,2,3,4,y1=3,y2="2",y3=1))
