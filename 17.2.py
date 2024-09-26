def dec2(a,b):

    def _dec2(fun):

        def __dec2(*args, **kwargs):

            y=fun(*args, **kwargs)
            if y<a or y>b:
                return a
            return y

        return __dec2
    return _dec2

@dec2(0,1)
def f1(x):
    return 2*x-1

@dec2(0,1)
def f2(x,y):
    return 2*x-y

if __name__=="__main__":

    print(f1(1), f1(0))
    print(f2(1,1), f2(0,5))
