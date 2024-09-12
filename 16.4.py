class EvenIterator:
    def __init__(self,seq):
        self.seq=seq
        self.current=len(self.seq)+len(self.seq)%2-2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current<0:
            raise StopIteration
        answer=self.seq[self.current]
        self.current-=2
        return answer
if __name__ == '__main__':
    lst=[0,1,2,3,4]
    even=EvenIterator(lst)
    for i in even:
        print(i)
