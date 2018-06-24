import math as m
def sigbit(a,k):
    s=[]
    a=int(a)
    while a>0:
        s.append(a%2)
        a=int(a/2)
    sa=s[len(s)-k:len(s)]
    r=0
    for i in range(k):
        r=r+sa[i]*(2**i)
    return r


def multiply(num,T):
    n=[1,1]
    n[0]=T[0][0]*num[0]+T[0][1]*num[1]
    n[1]=T[1][0]*num[0]+T[1][1]*num[1]
    num[0]=n[0]
    num[1]=n[1]


def bit(a):
    count=0
    while a>0:
       a=int(a/2)
       count=count+1
    return count


def mbit(T):
    m=T[0][0]
    for i in range(0,2):
        for j in range(0,2):
            if m<T[i][j]:
                m=T[i][j]
    count=bit(m)
    return count

def gcd(a,b):
    if b==o:
        return a
    else:
        return gcd(b,a%b)


def sf(nums,n):
    sf=1
    while n<=nums[1]:
        if nums[1]%n==0 and nums[0]%n==0:
            sf=sf*n
            nums[0]=nums[0]/n
            nums[1]=nums[1]/n
        else:
            break
    return sf
   
       

    
