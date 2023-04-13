class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        
        for i in range (len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            l, r = i + 1, len(nums) - 1
            while (l < r):
                if nums[l] + nums[r] < 0 - nums[i]:
                    l += 1
                elif nums[l] + nums[r] > 0 - nums[i]:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while (nums[l] == nums [l-1]) and (l < r):
                        l += 1 # The pairs are either duplicates or smaller than the target.
        return result