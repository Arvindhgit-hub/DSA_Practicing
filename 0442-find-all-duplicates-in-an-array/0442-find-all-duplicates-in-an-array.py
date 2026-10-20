class Solution(object):
    def findDuplicates(self, nums):
        n = len(nums)
        res = []
        for i in range(n):
            idx = abs(nums[i])-1
            if nums[idx] <0:
                res.append(idx +1)
            else:
                nums[idx] = -nums[idx]
        return res