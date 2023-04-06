class Sorted:
    def __init__(self,obj):
        self.obj=obj

    def __iter__(self):
        return iter(sorted(self.obj))

class SortedSet(Sorted, set):
    def __init__(self,obj):
         set.__init__(self,obj)
         Sorted.__init__(self,obj)

    def __str__(self):
        return f'{set.__str__(self)}'

s=SortedSet([4,2,3,1,12,8,7,10,9,5])
print(s)
