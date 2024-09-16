with open("file28.txt","r") as f:
    data=f.readlines()
toys=[]
prices=[]
for i in data:
    toy=i.split()
    name=toy[0]
    price=float(toy[1])
    lim1=float(toy[2])
    lim2=float(toy[3])
    toys.append((name,price,lim1,lim2))
    prices.append(price)
lstb=[]
for el in toys:
    if el[2]<=4 and el[3]>=10:
        lstb.append(el[0])
print(lstb)
lstv=[]
m=max(prices)-50
for el in toys:
    if el[1]>=m:
        lstv.append(el[0])
print(lstv)
