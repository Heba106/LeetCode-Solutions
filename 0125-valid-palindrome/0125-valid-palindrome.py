class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0;
        j = len(s) - 1
        while (i < j):
            if not (s[i].isalnum()):
                i += 1
                continue
            elif not (s[j].isalnum()):
                j -= 1
                continue
            if (s[i] != s[j]):
                return False
            print(s[i])
            print(s[j])
            i += 1
            j -= 1
    
        return True