class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hash_table = {}
        for el in strs:
            sorted_el = sorted(el)

            sorted_el = ''.join(sorted_el)
            if sorted_el in hash_table:
                hash_table[sorted_el].append(el)
            else:
                hash_table[sorted_el] = [el]
        

        return hash_table.values()