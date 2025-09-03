#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
            l=0
            r=len(letters)-1
            if target not in letters:
                return letters[0]
            while l<=r:
                mid=l+(r-l)//2
                if letters[mid]==target:
                    return letters[mid+1]
                if letters[mid]<=target:
                    l=mid+1
                else:
                    r=mid-1
            return 0      
# @lc code=end

