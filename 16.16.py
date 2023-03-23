#T = T * (-x**2)/ (2*k)/(2*k+1)
def xk_gen1(x, eps=0.0001):
    k=0
    x_k=x
    while abs(x_k)>eps:
        yield x_k
        x_k=x_k*(-x**2)/(2*k+3)/(2*k+2)
        k+=1

def xk_gen2(x, eps=0.0001):
    k=0
    x_k=1
    while abs(x_k)>eps:
        yield x_k
        x_k=x_k*(x**2)/(2*k+1)/(2*k+2)
        k+=1
        
if __name__=="__main__":
    x1=1
    s1=0
    a1=xk_gen1(x1)
    for i in a1:
        s1+=i
    print(s1)
    x2=1
    s2=0
    a2=xk_gen2(x2)
    for i in a2:
        s2+=i
    print(s2)
