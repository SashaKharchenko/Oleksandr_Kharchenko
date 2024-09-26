def sum(*x,**y):
    assert len(x) == len(y.keys()), f"size x should be equal to size y"
    Sum=0
    for i, key in enumerate(y.keys()):
        Sum += x[i]**2 + y[key]**2 + y[key]*x[i]
    return Sum

if __name__=='__main__':
    print(sum(1,2,3,y1=2,y2=3,y3=0))
    
