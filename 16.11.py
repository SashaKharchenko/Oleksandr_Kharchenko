class words1:
    def __init__(self,W):
        self.lst=W.split()
        self.index=-1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index>=len(self.lst)-1:
            raise StopIteration
        self.index+=1
        return self.lst[self.index]

class words2:
    def __init__(self,W):
        self.lst=W.split()
        self.rev=self.lst[::-1]
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index>=len(self.rev)-1:
            raise StopIteration
        self.index+=1
        return self.rev[self.index]
class words3:
    def __init__(self,W):
        self.lst=W.split()
        self.s=sorted(self.lst,key=len)
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index>=len(self.s)-1:
            raise StopIteration
        self.index+=1
        return self.s[self.index]
class words4:
    def __init__(self,W):
        self.lst=W.split()
        self.s=sorted(self.lst,key=len)[::-1]
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index>=len(self.s)-1:
            raise StopIteration
        self.index+=1
        return self.s[self.index]
class words5:
    def __init__(self,W):
        self.lst=W.split()
        self.index=-1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            self.index+=1
            if self.index>=len(self.lst):
                raise StopIteration
            if self.lst[self.index]==self.lst[self.index][::-1]:
                return self.lst[self.index]
if __name__=="__main__":
    string="qwq amog usu qwerty omor"
    for i in words1(string):
        print(i)
    print("\n")
    for i in words2(string):
        print(i)
    print("\n")
    for i in words3(string):
        print(i)
    print("\n")
    for i in words4(string):
        print(i)
    print("\n")
    for i in words5(string):
        print(i)
