import turtle
from math import sqrt
class Point2:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __str__(self):
        return "({}, {})".format(self._x, self._y)

class Point2Ex(Point2):

    def __init__(self,a,b):
        Point2.__init__(self,a,b)
        super().__init__(a,b)
        
    def __repr__(self):
        return f"P{self._x},{self._y}"
    
    def dist(self):
        return sqrt(self.get_x()**2+self.get_y()**2)
    
    def __eq__(self,p):
        return p.get_x()==self.get_x() and p.get_y()==self.get_y()
    
    def __lt__(self,p):
        return self.dist()<p.dist()
    
    def __add__(self,p):
        return Point2Ex(p.get_x()+self.get_x(),p.get_y()+self.get_y())

def dist2(a,b):
    return sqrt((b.get_x()-a.get_x())**2+(b.get_y()-a.get_y())**2)
if __name__=="__main__":
    lst=[]
    n=int(input("n="))
    for i in range(n):
        x=float(input(f"x{i}="))
        y=float(input(f"y{i}="))
        lst.append(Point2Ex(x,y))
    lst.sort()
    s=0
    for i in range(len(lst)):
        if i!=0:
            s+=dist2(lst[i-1],lst[i])
    print(s)
        
