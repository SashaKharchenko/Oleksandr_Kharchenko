dic={"RuntimeError":0,"TypeError":0,"ValueError":0}
lst=[]
while True:
    n=input("n=")
    if n=="досить":
        break
    lst.append(n)
for i in lst:
    if float(i)>9:
        dic["RuntimeError"]+=1
    elif float(i)<0:
        dic["TypeError"]+=1
    elif float(i)!=int(float(i)):
        dic["ValueError"]+=1
print(dic)
for i in lst:
    if float(i)>9:
        raise RuntimeError
    elif float(i)<0:
        raise TypeError
    elif float(i)!=int(i):
        raise ValueError
