#BRUTE FORCE
nums = [3,4,5,6]
target = 7
# for i in nums:
#     for j in nums:
#         if i+j == target:
#             print([i,j])
#             break

# OPTIMAL APPROACH

# by using a hashmap
prevmap={}
for i,n in enumerate(nums):
    diff=target-n
    if diff in prevmap:
        print([prevmap[diff],i])
    prevmap[n]=i


