try:
    f=open("content.txt")
except:
    raise FileNotFoundError("content.txt not found")
for el in f.readlines():
    el=el.strip("\n")
    el=el.strip(" ")
    try:
        e=open(el)
    except:
        raise FileNotFoundError(f"{el} not found")
    try:
        
        print(sum(list(map(float,e.read().split()))))
    except:
        raise TypeError(f"{e} має не лише дійсні числа")
    e.close()
f.close()
