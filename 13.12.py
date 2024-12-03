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

class Rectangle:

    def __init__(self,Apoint,width,height):
        self.A=Apoint
        self.w=width
        self.h=height

        self.B=Point2(self.A.get_x(),self.A.get_y()+height)
        self.C=Point2(self.A.get_x()+width, self.A.get_y()+height)
        self.D=Point2(self.A.get_x()+width,self.A.get_y())
    def getA(self):
        return self.A
    def getB(self):
        return self.B
    def getC(self):
        return self.C
    def getD(self):
        return self.D
    def area(self):
        return self.w*self.h
    def perimeter(self):
        return 2*(self.w+self.h)

    def __str__(self):
        return f"({self.A.get_x()},{self.A.get_y()}),\
({self.B.get_x()},{self.B.get_y()}),\
({self.C.get_x()},{self.C.get_y()}),\
({self.D.get_x()},{self.D.get_y()})"
    def intersect(self,rect):
        ax=max(self.A.get_x(),rect.A.get_x())
        ay=max(self.A.get_y(),rect.A.get_y())

        cx=min(self.C.get_x(),rect.C.get_x())
        cy=min(self.C.get_y(),rect.C.get_y())

        if cx>ax and cy>ay:
            A=Point2(ax,ay)
            return Rectangle(A,cx-ax,cy-ay)
        return None

if __name__=="__main__":
    spisokRect=[]
    n=int(input("n="))
    for _ in range(n):
        x=int(input("x:"))
        y=int(input("y:"))
        p=Point2(x,y)
        w=int(input("w:"))
        h=int(input("h:"))
        r=Rectangle(p,w,h)
        spisokRect.append(r)
    inters=spisokRect[0]
    for r in spisokRect:
        inters=inters.intersect(r)
        if inters==None:
            print("area = 0")
            break
    print("area =",inters.area())
    #p1=Point2Ex(
