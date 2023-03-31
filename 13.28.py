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
    '''
    def dist(self):
        return sqrt(self.get_x()**2+self.get_y()**2)
    '''
    def __eq__(self,p):
        return p.get_x()==self.get_x() and p.get_y()==self.get_y()
    '''
    def __lt__(self,p):
        return self.dist()<p.dist()
    
    def __add__(self,p):
        return Point2Ex(p.get_x()+self.get_x(),p.get_y()+self.get_y())
    '''
    def __ne__(self,p):
        return not self==p
    
class Segment:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def __str__(self):
        return "[{}, {}]".format(self._a, self._b)

    def len(self):
        return sqrt((self._a.get_x() - self._b.get_x())** 2 +
                    (self._a.get_y() - self._b.get_y())** 2)

class SegmentEx(Segment):
    def __init__(self,a,b):
        Segment.__init__(self,a,b)
        super().__init__(a,b)

    def __lt__(self,s):
        return self.len()<s.len()

    def __eq__(self,s):
        return self.len()==s.len()

    def eqLine(self,s):
        if (((self.a.get_y()-self.b.get_y())*(s.a.get_x()-self.b.get_x())==
        (s.a.get_y()-self.b.get_y())*(self.a.get_x()-self.b.get_x())) and
        ((self.a.get_y()-self.b.get_y())*(s.b.get_x()-self.b.get_x())==
        (s.b.get_y()-self.b.get_y())*(self.a.get_x()-self.b.get_x()))):
            return True
        return False
if __name__=="__main__":
    lst=[]
    n=int(input("n="))
    for _ in range(n):
        x1=float(input("x1="))
        y1=float(input("y1="))
        x2=float(input("x2="))
        y2=float(input("y2="))
        seg=SegmentEx(Point2Ex(x1,y1),Point2Ex(x2,y2))
        lst.append(seg)
        
    point_lst=[]
    for i in lst:
        point_lst.append(i.get_a())
        point_lst.append(i.get_b())
        
    isPoly=True
    isRegular=True
    
    for i in point_lst:
        if point_lst.count(i)!=2:
            isPoly=False
            print("Не многокутник")
            break
    if isPoly:
        for i in lst:
            if lst[0]!=i:
                isRegular=False
                print("Неправильний многокутник")
                break
        if isRegular:
            sx=0
            sy=0
            for i in point_lst:
                sx+=i.get_x()
                sy+=i.get_y()
            sx=sx/len(point_lst)
            sy=sy/len(point_lst)
            center=Point2Ex(sx,sy)
            lst2=[]
            for i in point_lst:
                seg=SegmentEx(i,center)
                if seg not in lst2:
                    lst2.append(seg)
            for i in lst2:
                if i!=lst2[0]:
                    isRegular=False
                    print("Неправильний многокутник")
                    break
            if isRegular:
                print("Правильний многокутник")
