class WeightedList(list):
    def __init__(self,lst=[]):
        list.__init__(self,lst)

    def weight(self):
        w=sum(map(abs,self))
        return w
    def __lt__(self,other):
        return self.weight()<other.weight()

class CompareMixin:
    def __eq__(self,other):
        if self<other or other<self:
            return False
        return True

    def __gt__(self,other):
        return other<self

    def __ne__(self,other):
        return not self==other

    def __ge__(self,other):
        return self==other or self>other

    def __le__(self,other):
        return self==other or self<other

class FullOrderWeightedList(CompareMixin, WeightedList):
    pass
if __name__=="__main__":
    n=int(input("n="))
    lists=[]
    isEqual=True
    for i in range(n):
        lst=input(f"list{i+1}=")
        lst=lst.split()
        lst=list(map(float,lst))
        lists.append(FullOrderWeightedList(lst))
    for lst in lists:
        if lst!=lists[0]:
            isEqual=False
            break
    print("isEqual =",isEqual)
    
