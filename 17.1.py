def make_positive(fun):

    def _make_positive(*args, **kwargs):

        y=fun(*args, **kwargs)
        if y<0:
            return 0
        return y

    return _make_positive

@make_positive
def f1(x):
    return 2*x-1

@make_positive
def f2(x,y):
    return 2*x-y

if __name__=="__main__":

    print(f1(1), f1(0))
    print(f2(1,1), f2(0,5))
