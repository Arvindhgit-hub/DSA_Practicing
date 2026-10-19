class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        res = set()
        for i in range(n):
            if i > k:
                res.remove(nums[i - k - 1])
            if nums[i] in res:
                return True
            res.add(nums[i])
        return False            



