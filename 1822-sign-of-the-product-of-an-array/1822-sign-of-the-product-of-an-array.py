class Solution:
    def arraySign(self, nums: List[int]) -> int:
        nums.sort()
        flag=0
        for _ in nums:
            if _>0:
                break
            elif _==0:
                return 0
            else:
                flag+=1
        return 1 if (flag%2==0) else -1
            