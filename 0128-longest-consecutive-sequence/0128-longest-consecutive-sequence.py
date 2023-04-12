class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        
        for el in nums:
            if (el - 1) not in nums:
                length = 1
                while (el + length) in nums:
                    length += 1
                longest = max (length, longest)
        return longest