

"""
with open('d2.in') as infile:
    cs = 0
    for line in infile:
        nums = [int(x) for x in line.split()]
        cs += max(nums) - min(nums)
    print cs
"""



def div_pair(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            n1 = nums[i]
            n2 = nums[j]
            if float(n1)/float(n2) == int(n1/n2):
                return n1/n2

with open('d2-2.in') as infile:
    cs = 0
    for line in infile:
        nums = sorted((int(x) for x in line.split()), key=lambda x: -x)
        cs += div_pair(nums)
    print cs
