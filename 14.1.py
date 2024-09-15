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

def sortStack(inputStack):

    lst=[]
    while not inputStack.isEmpty():
        d=inputStack.pop()
        lst.append(d)

    lst=sorted(lst)
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
    new_stack=sortStack(st)
    print(new_stack.data)
