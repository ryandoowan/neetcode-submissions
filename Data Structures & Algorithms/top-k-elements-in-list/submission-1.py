class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        
        res = []
        for key, v in d.items():
            if len(res) == 0:
                res.append((key,v))
            else:
                added = False
                for index, tup in enumerate(res):
                    if tup[1] > v:
                        res.insert(index, (key,v))
                        added = True
                        break
                    
                if not added:
                    res.append((key, v))
            
        ans = []
        for i in range(k):
            ans.append(res[len(res) - 1 - i][0])
        return ans