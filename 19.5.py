class TypeCheck:
    def __init__(self,cls):
        self.cls=cls
    def __call__(self, *args, **kwargs):
        for k,v in kwargs.items():
            if k not in self.cls._field_types:
                raise ValueError(f'Field{k} is not defined')
            if type(v)!=self.cls._field_types[k]:
                raise ValueError(f'Field{k} must be {self._field_types[k]}')
            return self.cls(*args, **kwargs)
@TypeCheck
class Point:
    _field_types={'x':int,'y':int}

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f'Point({self.x},{self.y})'

    def move(self,dx,dy):
        self.center.move(dx,dy)

@TypeCheck
class Circle:
    _field_types={'center':Point,'radius':int}

    def __init__(self,center,radius):
        self.center=center
        self.radius=radius

    def __str__(self):
        return f'Point({self.center},{self.radius})'

    def move(self,dx,dy):
        self.center.move(dx,dy)
if __name__=='__main__':
    p=Point(x=1,y=2)
    print(p)
    c=Circle(center=Point(x=1,y=2), radius=3)
    print(c)
    
