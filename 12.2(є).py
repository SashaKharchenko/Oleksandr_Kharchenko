with open("file.txt","r") as f:
    line=f.readline()
s=line.split()
list=[]
for i in s:
    list.append(float(i))
print(min(list)+max(list))
