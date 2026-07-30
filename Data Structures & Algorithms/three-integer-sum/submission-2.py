class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        ans = []
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                x = [nums[start], nums[end], nums[i]]
                if nums[start] + nums[end] + nums[i] == 0:
                    if x not in ans:
                        ans.append(x)
                
                if nums[start] + nums[end] <= -nums[i]:
                    start += 1
                elif nums[start] + nums[end] > -nums[i]:
                    end -= 1

        return ans