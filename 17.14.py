def dec(fun):
    def _dec(*args, **kwargs):
        lst=fun(*args, **kwargs)
        new_lst=[]
        for i in lst:
            if i not in new_lst:
                new_lst.append(i)
        return new_lst
    return _dec

@dec         
def f(fname):
    file=open(fname)
    q=file.read().split()
    file.close()
    return q
print(f("1714.txt"))
