def getValue(s,d):
    assert ((2<=d) and (d<=16)), f"{d} is not in 2..16"

    DIGITS=('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
    DIGIT_VAL=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

    result=0
    for c in s:
        if c.lower() not in DIGITS:           
            assert False, f"{c} is not correct digit for d={d}"
            return None
        index=DIGITS.index(c)

        if index>=d:
            assert False, f"{c} is not correct digit for d={d}"
            return None     
        digit=DIGIT_VAL[index]

        result =result*d+digit
    return result
if __name__=="__main__":

    s=input("Input number=")
    d=int(input("d="))
    n=getValue(s,d)
    print("n=",n)
