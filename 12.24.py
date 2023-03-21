with open("file.txt","r") as f:
    data=f.readlines()
cubes=[]
for i in data:
    cube=i.split(",")
    size=float(cube[0])
    color=cube[1].strip()
    material=cube[2].strip()
    cubes.append((size,color,material))
_colored={}
for cube in cubes:
    color=_colored.get(cube[1],[])
    color.append(cube)
    _colored[cube[1]]=color
colored={}
for k,v in _colored.items():
    colored[k]=(len(v),sum((map(lambda x:x[0]**3,v))))
print(colored)
counter={}
for cube in cubes:
    if cube[0]==3 and cube[2]=="wood":
        counter["wood"]=counter.get("wood",0)+1
    if cube[0]>5 and cube[2]=="metal":
        counter["metal"]=counter.get("metal",0)+1
print(counter)
