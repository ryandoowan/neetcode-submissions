class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

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