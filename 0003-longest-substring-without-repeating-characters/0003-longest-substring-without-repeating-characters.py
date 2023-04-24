class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr=[]
        max_count = 0
        count = 0
        
        for el in s:    
            if el in arr:
                arr = arr[arr.index(el)+1:]
                count = len(arr)

            arr.append(el)
            count += 1
            
            max_count = max(count, max_count)
        return max_count