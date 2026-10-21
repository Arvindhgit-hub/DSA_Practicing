class NumArray(object):

    def __init__(self, nums):
        self.prefix = []
        currentsum = 0
        for num in nums:
            currentsum += num
            self.prefix.append(currentsum)


    def sumRange(self, left, right):
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]    

        


