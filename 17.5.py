def dec(t):
    def _dec(fun):
        def __dec(*args,**kwargs):
            for arg in args:
                if not isinstance(arg,t):
                    raise TypeError("Wrong type")
            return fun(*args, **kwargs)
        return __dec
    return _dec

@dec(int)
def avg(*args):
    return sum(args)/len(args)
if __name__=="__main__":
    print(avg(2,3,5,7))
    print(avg(2,3,[[5],set()],7))
