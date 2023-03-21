class MultSet:

    def __init__(self):

        self.dct={}

    def makeEmpty(self):
        self.dct.clear()

    def isEmpty(self):
        return bool(self.dct)
    
    def addElement(self,el):
        self.dct[el]=self.dct.get(el,0)+1

    def popElement(self,el):
        self.dct[el]=self.gct.get(el,0)-1
        if self.dct[el]<=0:
            del self.dct[el]

    def countElement(self,el):
        return self.dct.get(el,0)

    def union(self,ms):
        keys1=set(self.dct.keys())
        keys2=set(ms.dct.keys())
        keys=keys1|keys2

        for it in keys:
            self.dct[it]=max(self.dct.get(it,0),ms.dct.get(it,0))

    def intersect(self,ms):
        keys1=set(self.dct.keys())
        keys2=set(ms.dct.keys())
        keys=keys1&keys2

        rem=keys1-keys2
        for it in rem:
            del self.dct[it]
        for it in keys:
            self.dct[it]=min(self.dct.get(it,0),ms.dct.get(it,0))
    def __str__(self):
        st="{"
        for k,v in self.dct.items():
            st += f"({k},{v}),"
        st+="}\n"
        return st
if __name__=="__main__":
    m1=MultSet()
    m1.addElement(1)
    m1.addElement(2)
    m1.addElement(2)
    m1.addElement(3)
    m1.addElement(3)
    m1.addElement(1)
    print(m1)
    m2=MultSet()
    m2.addElement(1)
    m2.addElement(3)
    m2.addElement(1)
    m2.addElement(3)
    m2.addElement(3)
    m2.addElement(4)
    print(m2)
    m1.union(m2)
    print(m1)

    q1=input("q1=")
    q2=input("q2=")
    w1=MultSet()
    w2=MultSet()
    for c in q1:
        w1.addElement(c)
    for c in q2:
        w2.addElement(c)
    w2.intersect(w1)
    print(w1,w2,w1.dct==w2.dct)
