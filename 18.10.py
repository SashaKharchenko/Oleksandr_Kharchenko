'''
зробив у класі
'''
from math import *
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return f'{self.x}, {self.y}'

    def input(self):
        self.x=float(input("x="))
        self.y=float(input("y="))

class CompareMixin:
    def __eq__(self,other):
        if self.__lt__(other) or other<self:
            return False
        return True

    def __gt__(self,other):
        if other<self:
            return True
        return False

    def __ne__(self,other):
        return not self==other

    def __ge__(self,other):
        return self==other or self>other

    def __le__(self,other):
        return self==other or self<other

class Point2(Point, CompareMixin):
    pass

class XOrderPoint2(Point2):
    def __lt__(self,other):
        return self.x<other.x

class DistOrderPoint2(Point2):
    def __lt__(self,other):
        dist1=sqrt(self.x**2+self.y**2)
        dist2=sqrt(other.x**2+other.y**2)
        return dist1<dist2
if __name__=="__main__":
    n=int(input("n="))
    lst=[]
    for i in range(n):
        a=DistOrderPoint2()
        a.input()
        lst.append(a)
    lst1=sorted(lst)
    for i in lst1:
        print(i)
    
        
