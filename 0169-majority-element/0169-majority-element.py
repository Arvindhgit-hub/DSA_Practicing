class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        n = len(nums)
        o = n//2
        return nums[o]
