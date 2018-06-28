from head import *
from DoAPhase import *
from DoAnIteration import *
from LongDivide import *
from math import *


A=int(input('Enter number A'))
B=int(input('Enter B'))

bits1=[bit(A)+bit(B)]
bits2=[]
n=bit(A)
nums=[]
nums.append(A)
nums.append(B)
sfs=1
for i in range(2,n):
    p=True
    if nums[1]==1:
        break
    if i==2:
        p=True
    else:
        for j in range(2,ceil(i**0.5)+1):
            if i%j==0:
                p=False
                break
    if p==True :
        sfs=sfs*sf(nums,i)

s=log(n,4)
s=s*s
s=2*s
s=int(s)
while bit(nums[0])>=s and bit(nums[1])>=s:
    DoAPhase(nums,n,bits1,bits2)
nums[0]=int(nums[0])
nums[1]=int(nums[1])
gd=gcd(nums[0],nums[1])
for i in range(2,n):
    p=True
    if gd==1:
        break
    if i==2:
        p=True
    else:
        for j in range(2,ceil(i**0.5)+1):
            if i%j==0:
                p=False
                break
    if p==True :
        while i<=gd:
            if gd%i==0 and (A%i!=0 or B%i!=0):
                gd=gd/i
            else:
                break
    
gd=gd*sfs
g=gcd(A,B)

print('\n',g,'\n',gd)
                
            
            

