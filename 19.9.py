def decClass(cls):
    def save(self, fname):
        f=open(fname,"w")
        for k,v in self.__dict__.items():
            f.write(v+"\n")
        f.close()
    def load(self, fname):
        f=open(fname,"r")
        r=f.read().split("\n")
        for i,k in enumerate(self.__dict__):
            self.__dict__[k]=r[i]
        f.close()
        return r
    cls.save=save
    cls.load=load
    return cls

@decClass
class twoStr:
    def __init__(self,a=None, b=None):
        self.a=a
        self.b=b
        
    def __str__(self):
        return self.a+" "+self.b
if __name__=="__main__":
    q=twoStr("Welcome","again")
    l=twoStr()
    q.save("file199.txt")
    l.load("file199.txt")  
    print(q)
    print(l)
