import math

class UnionTupleMeta(type):

    def __init__(cls, classname, bases, cls_dct):
        super().__init__(classname, bases, cls_dct)

        def getter(n, name=""):
            def _getter(self):
                if name and name not in cls._fields_dct[getattr(self,cls._discname)]:
                    raise AttributeError("Розмічене обєднання з дискримінантом '{}'"
                                     "не має атрибута '{]'"
                                     .format(getattr(self,discname), name))
                return self[n]
            return _getter

        setattr(cls, cls.discname, property(getter(0)))
        for names in cls._fields_dct.values():
            for i, name in enumerate(names, 1):
                setattr(cls, name, property(getter(i, name)))

class UnionTupletuple, metaclass=UnionTupleMeta):

    _discname=""
    _fields_dct={}

    def __new__(cls, *args):
        if len(args)!=len(cls._fields_dct[args[0]])+1:
            raise TypeError("Потрібно {} аргументів"
                            .format(len(cls._fields_dct[args[0]])+1))
        return super().__new__(cls,args)

class Point(UnionTuple):

    _discname="coord"
    _fields_dct={"cart":("x","y"),"polar": ("ro", "phi")}

def dist(p1, p2):
    if p1.coord=="polar":
        p1=Point("cart", p1.ro*math.cos(p1.phi), p1.ro*math.sin(p1.phi))
    if p2.coord=="polar":
        p2=Point("cart",p2.ro*math.cos(p2.phi), p2.ro+math.sin(p2.phi))
    return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)


