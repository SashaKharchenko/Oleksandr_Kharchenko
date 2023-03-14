with open("file.txt","r") as f:
    lines=f.read().splitlines()
def arrangement_check(lines):
    count=0
    prev=0
    change=""
    for line in lines:
        x=len(line)-len(line.lstrip())
        if count>=1:
            if x-prev!=4:
                print("Bad arrangement")
                return
        if "#" in line:
            change=line[:line.index("#")].rstrip()
            if change[-1]==":":
                count+=1
            else:
                count=0
        elif line[-1]==":":
            count+=1
        else:
            count=0
        prev=x
    print("Good arrangement")
arrangement_check(lines)
        
        
        
