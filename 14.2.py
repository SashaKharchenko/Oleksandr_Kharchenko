from collections import deque
class Stack:
    def __init__(self):
        self.data=deque()

    def isEmpty(self):
        return not self.data

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()
def lenStack(inputStack):

    i=0
    s=Stack()
    s.data=inputStack.data.copy()
    while not s.isEmpty():
        d=s.pop()
        i+=1
    return i
        

def invStack(inputStack):

    lst=[]
    s=Stack()
    s.data=inputStack.data.copy()
    while not s.isEmpty():
        d=s.pop()
        lst.append(d)

    result=Stack()
    for el in lst:
        result.push(el)
    return result
if __name__=="__main__":

    n=int(input("n="))
    st=Stack()
    for _ in range(n):
        el=float(input("x="))
        st.push(el)
    l=lenStack(st)
    new_stack=invStack(st)
    print(l)
    print(new_stack.data)
