class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if len(nums) == 0:
            return 0
        nums = [nums[0]] + nums + [nums[-1]]
        ans = []
        for i in range(1, len(nums) - 1):
            if nums[i-1]<=nums[i]>=nums[i+1]:
                return i-1
