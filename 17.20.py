def typechecker(*types):
    def _typechecker(f):
        def __typechecker(*args,**kwargs):
            if len(args)!= len(types):
                raise TypeError('Amount of arguments is wrong')
            for arg,type in zip(args, types):
                if not isinstance(arg,type):
                    raise TypeError("Wrong type")
            return f(*args, **kwargs)
        return __typechecker
    return _typechecker

@typechecker(str,int)
def mult(a,b):
    return a*b
if __name__=="__main__":
    print(mult("e",5))
    print(mult(3,5))
    print(mult(3,5,8))
