from random import randint
class Deque:
    
    def __init__(self,lst=[]):
        self.lst=lst

    def isEmpty(self):
        if self.lst==[]:
            return True
        return False

    def push(self,el):
        self.lst.append(el)

    def pop(self):
        a=self.lst.pop()
        return a

    def pushl(self,el):
        self.lst=[el]+self.lst

    def popl(self):
        a=self.lst[0]
        self.lst=self.lst[1:]
        return a
    
class Stack:
    def __init__(self,data=[]):
        self.data=Deque(data)

    def isEmpty(self):
        return self.data.isEmpty()

    def push(self, el):
        self.data.push(el)

    def pop(self):
        return self.data.pop()

    def __repr__(self):
        return str(self.data.lst)

def copyStack(st):
    return Stack(st.data.lst.copy())

def length(st):
    new_st=copyStack(st)
    i=0
    while not new_st.isEmpty():
        new_st.pop()
        i+=1
    return i

def inv(st):
    new_st=copyStack(st)
    newer_st=Stack()
    while not new_st.isEmpty():
        a=new_st.pop()
        newer_st.push(a)
    return newer_st

def dec(st):
    r=randint(0,3)
    if r==0:
        print(st.pop())
    elif r==1:
        st.push(float(input("n=")))
    elif r==2:
        print(st.data.popl())
    elif r==3:
        st.data.pushl(float(input("n=")))

if __name__=="__main__":
    a=[1,2,3]
    b=Stack(a)
    print("len b =",length(b))
    dec(b)
                 
    c=copyStack(b)
    print("copy =",c)
    dec(b)
                 
    print("inv =",inv(b))
    dec(b)        
    print(b)
