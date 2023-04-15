class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        result = 0
        
        while i < j:
            result = max(result,min(height[i],height[j])*(j-i))
            if height[j] < height[i]:
                j -= 1;
            elif height[i] <= height[j]:
                i += 1
        return result