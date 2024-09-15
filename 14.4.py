from collections import deque
from random import randint
class Queue:
    def __init__(self):
        self.data=deque()

    def isEmpty(self):
        return not self.data

    def push(self, element):
        self.data.append(element)

    def popl(self):
        return self.data.popleft()

    def length(self):
        counter=0
        tmp=Queue()
        while not self.isEmpty():
            el=self.popl()
            tmp.push(el)
            counter+=1
        self.data=tmp.data
        return counter

def inputQueue():

    count=0
    que=Queue()
    while True:
        try:
            x=int(input(f"x{count}="))
            que.push(x)
            count+=1
            if count>=10:
                break
        except:
            break
    return que

def recursiveLength(q):

    if q.isEmpty():
        return 0

    d=q.popl()
    r=1+recursiveLength(q)
    q.push(d)
    return r
if __name__=="__main__":
    n=int(input('n='))
    r=[]
    for x in range(n):
        r.append(randint(0,1))

    q=Queue()
    m=int(input('m='))
    for x in range(m):
        num=int(input(f'x{x+1}='))
        q.push(num)
    for b in r:
        if b:
            el=int(input('el='))
            q.push(el)
        else:
            print(q.popl())
    print(q.data)
    
