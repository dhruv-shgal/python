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
def next_greatest_letter(letters, target):
   l, r = 0, len(letters) - 1
   while l <= r:
            mid = l + (r - l) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        
   return letters[l] if l < len(letters) else letters[0]    


        



letters = ['c', 'f', 'j']
target='d'
print(next_greatest_letter(letters,target))
