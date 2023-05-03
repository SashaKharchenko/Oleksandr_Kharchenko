def paragraphs(s):
    lst=s.split("\n\n")
    new_lst=[]
    for i in lst:
        i=i.strip("\n")
        i=i.replace("\n"," ")
        if i:
          for j in ".,:;-!?_«»…":
              i=i.replace(j,"")
          i=i.replace("'","")
          i=i.replace('"',"")
          
          if i:
              new_lst.append(i)
              
    return new_lst

def getWord(lst,n,m):
        words=lst[n-1].split()
        return words[m-1]

def getCipher(fname):
    with open(fname,"r",encoding="utf-8") as f:
        cipher=f.read().split("\n")
        s=""
        for i in cipher:
            s=s+i+" "
        s=s.split()
        dct=[]
        for i in range(0,len(s),2):
            dct.append((int(s[i]),int(s[i+1])))
        return dct

def decipher(fcipher, ftext):
    s=""
    dct=getCipher(fcipher)
    with open(ftext,"r",encoding="utf-8") as f:
        cont=f.read()
    pars=paragraphs(cont)
    
    for k in dct:
        word=getWord(pars,k[0],k[1])
        s=s+word+" "
    return s

if __name__=="__main__":
    print(decipher("cipher_13.txt", "group_13.txt"))
