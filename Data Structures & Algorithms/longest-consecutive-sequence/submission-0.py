class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        ans = 0
        for i in nums:
            if (i - 1) not in s:
                count = 1
                num = i + 1
                while True:
                    if num in s:
                        count += 1
                        num += 1
                    else:
                        break
                if count > ans:
                    ans = count

        return ans

