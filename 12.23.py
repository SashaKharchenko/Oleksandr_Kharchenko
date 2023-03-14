with open("file23.txt","r") as f:
    data=f.read().splitlines()
name=input("Прізвище та ініціали=")
lst=name.split()
for el in data:
    worker=el.split()
    if worker[0]==lst[0] and worker[1]==lst[1] and worker[2]==lst[2]:
        print(worker[3])
        break
