class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        stack = []
        for el in s:
            if el not in hash_map:
                stack.append(el)
                continue
            else:
                if len(stack) == 0 or stack[-1] != hash_map[el]:
                    return False
                stack.pop()

        return not stack
