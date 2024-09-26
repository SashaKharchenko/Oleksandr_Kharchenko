def diag(matr):
    assert len(matr)==len(matr[0]), "matr has to be a square matrix"
    i=0
    while i<len(matr):
        yield matr[i][i]
        i+=1
if __name__=="__main__":
    matrix=[[1,2,3],[3,2,1],[2,2,0]]
    gen=diag(matrix)
    s=0
    for el in gen:
        s+=el
    print(s)
