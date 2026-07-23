class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        # if len(piles) == 1:
        #     if piles[0] % h == 0:
        #         return piles[0] // h
        #     else:
        #         return piles[0] // h + 1
        while start < end:
            hours = 0
            mid = (start + end) // 2
            for i in piles:
                hours += i // mid
                if i % mid != 0:
                    hours += 1
            
            if hours > h:
                start = mid + 1
            else:
                end = mid
            
        return start