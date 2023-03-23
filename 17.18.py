from collections import Counter

def dec(fun):

    def _dec(*args, **kwargs):
        lst=[]
        dic={}     
        for arg in args:
            lst.append(arg.lower())
        for k,v in kwargs.items():
            dic[k]=v.lower()
        return fun(*lst, **dic)
    return _dec

@dec        
def count(s):
    c=Counter()
    for Chara in s:
        c[Chara]+=1
    return c

if __name__=="__main__":
    print(count("aSDfdsASas"))
