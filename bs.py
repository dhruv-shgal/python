# grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]] 
# m,n=len(grid),len(grid[0])
# count=0
# for row in grid:
#     l,r=0,n-1
#     while l<=r:
#         mid=l+(r-l)//2
#         if row[mid]>0:
            
#             l=mid+1
#         else:
#             r=mid-1
#     count+=n-l
# print(count)        
# 
#   
# def next_greatest_letter(letters, target):
#    l, r = 0, len(letters) - 1
#    while l <= r:
#             mid = l + (r - l) // 2
#             if letters[mid] <= target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
        
#    return letters[l] if l < len(letters) else letters[0]    


        



# letters = ['c', 'f', 'j']
# target='d'
# print(next_greatest_letter(letters,target))

def searchRange(nums, target):
    l=0
    h=len(nums)-1
    res=-1
    while(l<=h):
        mid=l+(h-l)//2
        if nums[mid]==target:
            res=mid
            h=mid-1
        elif nums[mid]<target:
            l=mid+1
        else:
            h=mid-1
    return res        
def last_index(nums,target):
    l=0
    h=len(nums)-1
    res1=-1
    while(l<=h):
        mid=l+(h-l)//2
        if nums[mid]==target:
            res1=mid
            l=mid+1
        elif nums[mid]<target:
            l=mid+1
        else:
            h=mid-1
    return res1  
    


nums=[5,7,7,8,8,10]
target=8
first=searchRange(nums,target)
last=last_index(nums,target)
print(f"Number = {target}, the first index is {first} and the last index is {last}")
