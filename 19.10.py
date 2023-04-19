import math

def union(classname, discname,dct):
    cls_dct={}

    def getter(n, name=""):
        def _getter(self):
            if name and name not in dct[getattr(self,discname)]:
                raise AttributeError("Розмічене обєднання з дискримінантом '{}'"
                                     "не має атрибута '{]'"
                                     .format(getattr(self,discname), name))
            return self[n]
        return _getter

    cls_dct[discname]= property(getter(0))
    for names in dct.values():
        for i, name in enumerate(names, 1):
            cls_dct[name]=property(getter(i, name))

    def __new__(cls, *args):
        if len(args)!=len(dct[args[0]])+1:
            raise TypeError
        return tuple.__new__(cls, args)

    cls_dct["__new__"]= __new__

    cls=type(classname, (tuple,), cls_dct)
    return cls

def dist(p1, p2):
    if p1.coord=="polar":
        p1=Point("cart", p1.ro*math.cos(p1.phi), p1.ro*math.sin(p1.phi))
    if p2.coord=="polar":
        p2=Point("cart",p2.ro*math.cos(p2.phi), p2.ro+math.sin(p2.phi))
    return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)
        
