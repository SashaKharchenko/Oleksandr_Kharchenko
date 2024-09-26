def partial_sort(fname, n, gname):
    assert n>0, "n must be natural"
    new_list=[]
    try:
        f=open(fname,"r")
        s=f.readline()
        a=s.split()
        for i in a:
            element=int(i)
            new_list.append(element)
        g=open(gname,"w")
        j=0
        lst=[]
        while j <len(new_list):
            m=max(new_list[j:(j+n)])
            lst.append(m)
            j+=n
        print(" ".join([str(x) for x in lst]),file=g)
        print("\n", file=g)
        g.close()
        f.close()
    except FileNotFoundError as e:
        print("No File?",e)
        return False
    except IOError as e:
        print("Cannot read from file",e)
        return False
    except ValueError as e:
        print("Can't convert to int",e)
        return False
    except AssertionError as e:
        print("Assert error",e)
        return False
    return True
if __name__=="__main__":
    partial_sort("f.txt",3,"g.txt")
        
