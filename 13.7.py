class Segment:
    __slots__ = ("a","b","empty")
    
    def __init__(self,a,b,empty):
        self.a=a
        self.b=b
        self.empty=empty if empty is not None else False

    def __repr__(self):
        return f'Segment({self.a}, {self.b}, {self.empty})'

    def set_empty(self):
        self.empty=True

    @property
    def is_empty(self):
        return self.empty

    @classmethod
    def new_segment(cls, a,  b):
        if a>b:
            return cls(empty=True)
        return cls(a,b,False)

    @classmethod
    def intersection(cls, *segments):
        if any(s.empty for s in segments):
            return cls(empty=True)
        else:
            a=max(s.a for s in segments)
            b=min(s.b for s in segments)
            if a>b:
                return cls(empty=True)
            else:
                return cls(a, b, False)
if __name__=="__main__":
    n=int(input("n="))
    segments=[]
    emp=False
    for i in range(n):
        p=int(input("p{}=".format(i+1)))
        q=int(input("q{}=".format(i+1)))
        D=p**2-4*q
        if D<=0:
            emp=True
            print("Немає розв'язків")   
            break
        x1=(-p-D)/2
        x2=(-p+D)/2
        segments.append(Segment(x1,x2,False))
    if not emp:
        print(Segment.intersection(*segments))
        

