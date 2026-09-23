class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nums = []
        l, r = 0, len(heights) - 1
        while l < r:
            highest = (r - l) * min(heights[l], heights[r])
            nums.append(highest)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return max(nums)

            

            
            

        