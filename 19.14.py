import time
def decTime(fun):
    def _decTime(*args, **kwargs):
        a=time.perf_counter()
        res=fun(*args,**kwargs)
        b=time.perf_counter()-a
        print("{0} time elapsed {1:.8f}".format(fun.__name__,b))
        return res
    return _decTime

class Meta(type):
    
    def __init__(cls, classname,bases, cls_dct):
        super().__init__(classname, bases, cls_dct)
        for k,v in cls_dct.items():
            if callable(v):
                setattr(cls,k,decTime(v))

class Btree(metaclass=Meta):
    def __init__(self):
        self._data = None
        self._ls = None
        self._rs = None

    def isempty(self):
        return self._data == None and self._ls == None and self._rs == None

    def maketree(self, data, t1, t2):
        self._data = data
        self._ls = t1
        self._rs = t2

    def root(self):
        if self.isempty():
            print('root: Дерево порожнє')
            exit(1)
        return self._data

    def leftson(self):
        if self.isempty():
            t = self
        else:
            t = self._ls
        return t

    def rightson(self):
        if self.isempty():
            t = self
        else:
            t = self._rs
        return t

    def updateroot(self, data):
        if self.isempty():
            self._ls = Btree()
            self._rs = Btree()
        self._data = data

    def updateleft(self, t):
        self._ls = t

    def updateright(self, t):
        self._rs = t

def makeSearchTree(data):
    b=Btree()
    b.updateroot(data)
    ls=float(input("ls="))
    if ls<=data:
        b.updateleft(makeSearchTree(ls))
    rs=float(input("rs="))
    if rs>=data:
        b.updateright(makeSearchTree(rs))
    return b
if __name__=="__main__":
    r=float(input("root="))
    q=makeSearchTree(r)
