class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if i < 0:
                i *= -1
            
            if nums[i] < 0:
                return i
            else:
                nums[i] *= -1
            print(nums)
        return 0