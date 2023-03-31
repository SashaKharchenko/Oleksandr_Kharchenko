class IncorrectData(Exception):
    def __init__(self,n):
        self.n=n

    def __str__(self):
        return f'{self.n} is incorrect'

class FileProblem(Exception):
    def __init__(self, fname,msg):
        self.fname=fname
        self.msg=msg

    def __str__(self):
        return f'{self.f} is not open: {self.msg}'
class WorkBinFile:

    def __init__(self, fname):

        self.fname=fname
        self.num=0

    def inputConsole(self):

        n=int(input("n="))

        if n<=0:
            raise IncorrectData(n)

        f=open(self.fname, "wb")

        if not f:
            raise FileProblem(self.fname,"cannot open")

        for _ in range(n):
            x=int(input("x="))
            f.write(x)

        f.close()

    def writeFromList(self,lst):
        f=open(self.fname, "wb")
        if not f:
            raise FileProblem(self.fname,"cannot open")
        for x in lst:
            f.write(x)

        f.close()

    def read(self):
        f=open(self.fname, "rb")
        if not f:
            raise FileProblem(self.fname,"cannot read")
        while True:
            x=f.read(1)
            x=int.from_bytes(x, byteorder='big')
            print(x)
            if not x:
                break
        
        f.close()

    def append(self, data):
        f=open(self.fname, "a+b")
        if not f:
            raise FileProblem(self.fname,"cannot append")
        f.write(bytearray([data]))
        f.close()

if __name__=="__main__":
    try:
        wf=WorkBinFile("1.dat")
        wf.writeFromList([1,2,4,3,5,7,2])
        wf.append(8)
        wf.read()
    except FileProblem as e:
        print(e)
        
