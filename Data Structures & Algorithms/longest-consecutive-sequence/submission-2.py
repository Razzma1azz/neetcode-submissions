class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in numSet:
                current_length = 1
                while num + current_length in numSet:
                    current_length += 1

                if current_length > longest:
                    longest = current_length
        
        return longest