class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)
        result = []

        for num in nums:
            mapping[num] += 1
        
        #returns list of keys sorted based on their values
        sorted_dict = sorted(mapping, key=mapping.get, reverse=True) 

        return sorted_dict[:k]