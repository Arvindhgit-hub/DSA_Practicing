class Solution(object):
    def buildArray(self, target, n):
        result = []
        current = 1
        for i in target:
            while current < i:
                result.append("Push")
                result.append("Pop")
                current += 1
            result.append("Push")
            current += 1
        return result        
