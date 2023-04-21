from abc import ABCMeta, abstractmethod
from math import *
class Shape(metaclass = ABCMeta):

    @abstractmethod
    def perimeter(self):
        raise NotImplementedError

    @abstractmethod
    def area(self):
        raise NotImplementedError

    @abstractmethod
    def intersect(self):
        raise NotImplementedError
    
class Circle(Shape):

    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
        
    def perimeter(self):
        return 2*pi*self.r

    def area(self):
        return pi*self.r**2

    def intersect(self,other):
        if isinstance(other, Circle):
            return (other.x-self.x)**2+(other.y-self.y)**2<(self.r+other.r)**2

        return False

class Rectangle(Shape):

    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        
    def perimeter(self):
        return 2*(self.h+self.w)

    def area(self): 
        return self.h*self.w

    def intersect(self,other):
        if isinstance(other, Rectangle):
            x1=max(other.x,self.x)
            x2=min(other.x+other.w,self.x+self.w)

            y1=max(other.y,self.y)
            y2=min(other.y+other.h,self.y+self.h)

            if x1<=x2 and y1<=y2 :
                return True
            else:
                return False

        elif isinstance(other, Circle):
            return False
        return False
if __name__=="__main__":

    n=int(input("Number of figures:"))
    figures=[]

    for i in range(n):
        choice=input("Input rect(r) or circle(c), or exit(q)")

        CHOICES=("r","c","q")
        while choice not in CHOICES:
            choice=input("Input rect(r) or circle(c), or exit(q)")
        if choice=="c":
            x,y,r=map(float,input().split())
            c=Circle(x,y,r)
            figures.append(c)
        elif choice=="r":
            x,y,w,h=map(float,input().split())
            r=Rectangle(x,y,w,h)
            figures.append(r)
        else:
            break
    sum_area=0
    for item in figures:
        sum_area+=item.area()

    sum_area1=sum([f.area() for f in figures])

    print(f"sum area {sum_area}, {sum_area1}")
