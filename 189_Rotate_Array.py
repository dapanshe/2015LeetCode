class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if nums == []:
            return []
        length = len(nums)
        k = k % length
        left = nums[:length - k]
        right = nums[length - k:]
        for i in range(0, k):
            nums[i] = right[i]
        for i in range(0,length - k):
            nums[i+k] = left[i]
