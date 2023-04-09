class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr = set()
        for x in nums:
            if x  in arr:
                return True
            else:
                arr.add(x)