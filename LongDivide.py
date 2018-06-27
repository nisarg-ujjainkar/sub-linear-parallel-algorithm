from head import *
from math import *
def LongDivide(nums):
    k=bit(nums[0])-bit(nums[1])
    a=sigbit(nums[0],2*k)
    b=sigbit(nums[1],k)
    q=int(a/b)
    C=nums[0]-q*nums[1]
    nums[0]=nums[1]
    nums[1]=C
    print(nums)

