from head import *
from math import *
def DoAnIteration(nnums,T,n):
    a=nnums[0]
    b=nnums[1]
    l=bit(a)-bit(b)
    p=0-ceil(n*b/a)
    q=0
    if a>=(b*n):
        q=int(a/b)
        p=1
    else:
        while p<=ceil(n*b/a):
            if p!=0:
                q=int(p*a/b)
                r=p*a-q*b
                if r>=0 and r<=int(2*a/n):
                    break
            p=p+1
    print(p,'\t',q)
    t=[[1,0],[0,1]]
    t[0][0]=0*T[0][0]+1*T[1][0]
    t[0][1]=0*T[0][1]+1*T[1][1] 
    t[1][0]=p*T[0][0]-q*T[1][0]
    t[1][1]=p*T[0][1]-q*T[1][1]
    T[0][0]=t[0][0]
    T[1][0]=t[1][0]
    T[0][1]=t[0][1]
    T[1][1]=t[1][1]
    multiply(nnums,T)
    
            
            
