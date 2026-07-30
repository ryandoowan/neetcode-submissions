class Solution:
    from collections import defaultdict
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = sorted(hand)

        d = defaultdict(int)
        for i in hand:
            d[i] += 1

        for j in hand:
            if d[j] == 0:
                continue

            num = j
            for k in range(groupSize):
                if d[num] > 0:
                    d[num] -= 1
                    num += 1
                else:
                    return False
        
        return True
                 