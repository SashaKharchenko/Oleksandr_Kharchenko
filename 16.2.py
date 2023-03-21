class InvEven:
    def __init__(self,n):
        self.n=n
        self.current=n+2-n%2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current<=0:
            raise StopIteration
        self.current-=2
        return self.current
if __name__ == '__main__':
    n=InvEven(6)
    for i in n:
        print(i)
