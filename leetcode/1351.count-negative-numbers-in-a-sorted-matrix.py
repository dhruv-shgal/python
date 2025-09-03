#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        count=0
        for row in grid:
            l,r=0,n-1
            while l<=r:
                mid=l+(r-l)//2
                if row[mid]>=0:
                    
                    l=mid+1
                else:
                    r=mid-1
            count+=n-l
        return count    
# @lc code=end

