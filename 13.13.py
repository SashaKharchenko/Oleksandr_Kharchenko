from math import *
class Point2:
    
    def __init__(self, x, y):
        self._x = x
        self._y = y

    
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __str__(self):
        return "({},{})".format(self._x, self._y)

class RegularPolygone:

    def __init__(self, lst):
        self.lst=lst

    def get_lst(self):
        return self.lst

    def perimeter(self):
        dist=sqrt((self.lst[0].get_x()-self.lst[1].get_x())**2+(self.lst[0].get_y()-self.lst[1].get_y())**2)
        return dist*len(self.lst)

    def area(self):
        dist=sqrt((self.lst[0].get_x()-self.lst[1].get_x())**2+(self.lst[0].get_y()-self.lst[1].get_y())**2)
        height=dist/(2*tan(pi/(len(self.lst))))
        return height*dist*len(self.lst)/2

    def __str__(self):
        list=[]
        for i in self.lst:
            list.append((i.get_x(),i.get_y()))
        return f"{list}"
def center(Poly):
    sx=0
    sy=0
    for i in Poly.get_lst():
        sx+=i.get_x()
        sy+=i.get_y()
    sx=sx/len(Poly.get_lst())
    sy=sy/len(Poly.get_lst())
    return Point2(sx,sy)
def dist(start,end,point):
    A=end.get_y()-start.get_y()
    B=start.get_x()-end.get_x()
    C=start.get_y()*(end.get_x()-start.get_x())-start.get_x()*(end.get_y()-start.get_y())
    return (A*point.get_x()+B*point.get_y()+C)/sqrt(A**2+B**2)
def InPolygone(Point,Poly):
    c=center(Poly)
    for i in range(len(Poly.get_lst())):
        s=Poly.get_lst()[i]
        if i!=len(Poly.get_lst())-1:
            e=Poly.get_lst()[i+1]
        else:
            e=Poly.get_lst()[0]
        if dist(s,e,Point)*dist(s,e,c)<0:
            return False
    return True
def union(Poly1,Poly2):
    if Poly1.get_lst()==[] or Poly2.get_lst()==[]:
        return RegularPolygone([])
    for i in Poly1.get_lst():
        if not InPolygone(i,Poly2):
            for i in Poly2.get_lst():
                if not InPolygone(i,Poly1):
                    return RegularPolygone([])
            return Poly1
    return Poly2
if __name__=="__main__":
    Polygones=[]
    n=int(input("Кількість многокутників="))
    for i in range(n):
        m=int(input("Кількість вершин="))
        lst=[Point2(float(input(f"x{i+1}=")),(float(input(f"y{i+1}=")))) for i in range(m)]
        Polygones.append(RegularPolygone(lst))
    for el in Polygones:
        un=el
        for i in Polygones:
            un=union(un,i)
            if un.get_lst()==[]:
                continue
        if un!=[]:
            break
    print(un)
