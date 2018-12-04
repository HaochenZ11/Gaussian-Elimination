#forward step of Gaussian Elimination
def ge_fw(matrix):
    try:
        r=len(matrix)-1
        c=len(matrix[0])-1
        if r <0 or c<0:
            return -1
    except:
        return -1
    rowm=0
    first=0
    firstr=0
    firstc=0
    sum=4
    mult=1
    temp=[]
    zero=0
    while (firstr != r and firstc !=c):       
        #finds first nonzero row
        for i in range(firstr,r+1, 1):          
            if matrix[i][firstc] != 0:
                temp = list(L[firstr])
                L[firstr] = list(L[i])
                L[i] = list(temp)
                break  
        
        #add multiples of a row to another 
        first = matrix[firstr][firstc]
        for i in range(firstr+1,r+1,1):
            if first != 0.0:
                mult = (0-matrix[i][firstc])/first
                for k in range(firstc,c+1,1):
                    matrix[i][k] = matrix[i][k] +matrix[firstr][k]*mult
       
        #step performed until no more submatrices            
        firstr = firstr+1
        firstc = firstc+1
      

#backwards step in Gaussian elimination
def ge_bw (matrix):
    try:
        r=len(matrix)-1
        c=len(matrix[0])-1
        if r<0 or c <0:
            return -1
    except:
        return -1
    lastr=r
    lastc=c
    nz=False
    normal=1
    col=0
    sum=0
    zero=False
    temp=[]
    print("back")
    while lastr >= 0 and lastc >= 0:
        #finds zero rows
        for k in range(0,r+1,1):
            for i in range(0,c+1,1):
                if matrix[k][i] != 0:
                    zero=False
                    break
                else:
                   zero= True
            if zero == True:
                temp=list(L[k])
                L[k]=list(L[r])
                L[r] = list(temp)           
        #finds last nonzero row
        for k in range(lastr,-1,-1):
            nz=False
            for i in range(0,c+1,1):
                if matrix[k][i] != 0:
                    nz =True
                else:
                    nz=False
            if nz == True:
                lastr=k
                break
        for j in range(0,c+1,1): #finds the nonzerovalue
            #print(lastr)
            #print(j)
            if matrix[lastr][j] != 0:
                col=j
                normal = 1/matrix[lastr][j]
                for z in range(j,c+1,1):
                    matrix[lastr][z]=matrix[lastr][z]*normal
                break
        for k in range(lastr-1,-1,-1): #makes terms above a zero
           if matrix[k][col] != 0.0:
                mult = (0-matrix[k][col])
                for x in range(0,c+1,1):
                    matrix[k][x] = matrix[k][x] +matrix[lastr][x]*mult  
        lastr=lastr-1
        lastc=lastc-1
    return matrix


