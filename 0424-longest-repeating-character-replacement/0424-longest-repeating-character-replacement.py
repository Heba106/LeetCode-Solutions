class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        result = 0
        l = 0
        maxf = 0
        
        for r in range (len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxf = max(maxf, freq[s[r]])
            if (r-l+1)-maxf > k:
                freq[s[l]] -=1
                l +=1
            result = max(result, r-l+1)
        return result