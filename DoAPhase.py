from math import *
from head import *
from DoAnIteration import *
from LongDivide import *
def DoAPhase(nums,n,bits1,bits2):
    s=log(n,4)
    s=s*s
    s=int(s)
    s=s*2

    if bit(nums[0])<bit(nums[1]):
        m=bit(nums[1])
    else:
        m=bit(nums[0])
    if nums[0]<nums[1]:
        temp=nums[0]
        nums[0]=nums[1]
        nums[1]=temp
    if (bit(nums[0])-bit(nums[1]))>int(s/2):
        LongDivide(nums)
    else:
        T=[[1,0],[0,1]]
        nnums=[]
        a=sigbit(nums[0],s)
        k=s-(bit(nums[0])-bit(nums[1]))
        b=sigbit(nums[1],k)
        nnums.append(a)
        nnums.append(b)
        endsize=bit(nnums[0])+bit(nnums[1])-int(s/2)
        while (bit(nums[0])+bit(nums[1])>=endsize) and (mbit(T)<=int(s/2)):            
            DoAnIteration(nnums,T,n,bits2)
        multiply(nums,T)
    bits=bit(nums[0]+nums[1])    
        
        
    
