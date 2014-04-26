import numpy as np

M = 0
N = 0

dbg = False

def loadCore(filename):
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    
    maxi = 0
    maxj = 0
        
    for line in lines:
        l = line.split(',')
        i = int(l[0])
        j = int(l[1])
        if i>maxi: maxi=i
        if j>maxj: maxj=j
    
    M = maxi+1
    N = maxj +1
    arr = np.empty((M,N))
    
    
    for line in lines:
        l = line.split(',')
        l = [int(ll.strip()) for ll in l]
        arr[l[0],l[1]] = l[2]
    
    if dbg: print(arr)
    return arr

if __name__=='__main__':
    loadCore('default.core')
        
        