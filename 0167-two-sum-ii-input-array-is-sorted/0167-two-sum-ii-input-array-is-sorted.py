class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        left = 0
        right = n-1
        while left < right:
            currentsum = numbers[left] + numbers[right]
            if currentsum == target:
                return [left+1,right+1]
            elif currentsum < target:
                left +=1
            elif currentsum > target:
                right -=1        