class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        max_keys = []
        for el in nums:
            hash_table[el] = 1 + hash_table.get(el , 0)
        
        hash_table = dict(sorted(hash_table.items(), key=lambda item: item[1], reverse= True))
        for i, key in enumerate(hash_table.keys()):
            if i == k:
                break
            max_keys.append(key)
                
        return max_keys