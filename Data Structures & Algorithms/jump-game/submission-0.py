class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1):
            if ((nums[len(nums) - 2 - i] + len(nums) - 2 - i) >= goal):
                goal = len(nums) - 2 - i
        
        if goal == 0:
            return True
        else:
            return False