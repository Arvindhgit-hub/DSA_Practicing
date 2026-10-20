class Solution(object):
    def singleNumber(self, nums):
        n = len(nums)
        newset = set()
        for i in nums:
            newset.add(i)
        for j in newset:
            if nums.count(j) == 1:
                return j