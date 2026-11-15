class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        for leng in range(1,(n//2)+1):
            if n % leng == 0:
                substring = s[:leng]
                repeats = n // leng
                if substring * repeats == s:
                    return True
        return False            