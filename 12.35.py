with open("file35.txt","r") as f:
    lines=f.read().splitlines()
def starts(l,sym):
    i=0
    for c in l:
        if c[0]==sym:
            i+=1
    return i
def ends(l,sym):
    i=0
    for c in l:
        if c[-1]==sym:
            i+=1
    return i
def equal(l):
    i=0
    for c in l:
        if c[-1]==c[0]:
            i+=1
    return i
def one(l):
    i=0
    for c in l:
        if c.strip(c[0])=="":
            i+=1
    return i
if __name__=="__main__":
    print("а)",starts(lines,"e"))
    print("б)",ends(lines,"e"))
    print("в)",equal(lines))
    print("г)",one(lines))
