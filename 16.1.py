class EvenIterator:
    def __init__(self,n):
        self.n=n
        self.current=n%2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current> self.n:
            raise StopIteration
        answer=self.current
        self.current+=2
        return answer
if __name__ == '__main__':
    n=10
    even=EvenIterator(n)
    for i in even:
        print(i)
