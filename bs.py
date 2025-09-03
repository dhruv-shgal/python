grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]] 
m,n=len(grid),len(grid[0])
count=0
for row in grid:
    l,r=0,n-1
    while l<=r:
        mid=l+(r-l)//2
        if row[mid]>0:
            
            l=mid+1
        else:
            r=mid-1
    count+=n-l
print(count)          
