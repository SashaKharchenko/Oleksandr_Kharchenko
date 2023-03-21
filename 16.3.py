class EvenIterator:
    def __init__(self,seq):
        self.seq=seq
        self.current=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current>=len(self.seq):
            raise StopIteration
        answer=self.seq[self.current]
        self.current+=2
        return answer
if __name__ == '__main__':
    lst=[0,1,2,3,4,5]
    even=EvenIterator(lst)
    for i in even:
        print(i)
