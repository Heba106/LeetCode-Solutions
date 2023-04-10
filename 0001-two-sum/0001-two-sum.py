class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table ={}
        for i , n in enumerate(nums):
            diff = target - n
            if diff in hash_table:
                return[hash_table[diff], i]
            hash_table[n]= i