class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        total = 1
        nonzero = 1
        zeros = 0
        for i in nums:
            if i != 0:
                nonzero *= i 
            else:
                zeros += 1
            total *= i

        for j in nums:
            if j == 0:
                if zeros > 1:
                    ans.append(0)
                else:
                    ans.append(nonzero)
            else:
                ans.append(total // j)
        
        return ans