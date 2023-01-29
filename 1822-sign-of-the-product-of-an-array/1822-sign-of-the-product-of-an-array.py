class Solution:
    def arraySign(self, nums: List[int]) -> int:
        nums.sort()
        flag = True
        for _ in nums:
            if _>0:
                break
            elif _==0:
                return 0
            else:
                flag = not flag
        return 1 if (flag) else -1
            