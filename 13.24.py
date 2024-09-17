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
class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        
    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def get_c(self):
        return self._c

    def __str__(self):
        return "Трикутник ({}, {}, {})".format(self._a, self._b, self._c)

    def _get_sides(self):
        s1 = Segment(self._a, self._b).len()
        s2 = Segment(self._b, self._c).len()
        s3 = Segment(self._a, self._c).len()
        return s1, s2, s3

    def perimeter(self):
        s1, s2, s3 = self._get_sides()
        return s1 + s2 + s3

    def square(self):
        p = self.perimeter() / 2
        s1, s2, s3 = self._get_sides()
        return sqrt(p * (p - s1) * (p - s2) * (p - s3))

class TriangleEx(Triangle):
    def __init__(self,a,b,c):
        Triangle.__init__(self,a,b,c)
        super().__init__(a,b,c)
    def __lt__(self,t):
        return self.square()<t.square()
    def __eq__(self,t):
        return self.square()==t.square()
if __name__=="__main__":
    n=int(input("n="))
    lst=[]
    for i in range(n):
        P1=Point2(float(input("x1=")),float(input("y1=")))
        P2=Point2(float(input("x2=")),float(input("y2=")))
        P3=Point2(float(input("x3=")),float(input("y3=")))
        lst.append(TriangleEx(P1,P2,P3))
    lst.sort()
    for i in lst:
        print(i)
