class Solution(object):
    def maxVowels(self, s, k):
        vow = {'a','e','i','o','u'}
        current_vow = 0
        for i in range(k):
            if s[i]in vow :
                current_vow += 1
        max_vow = current_vow 

        for i in range(k, len(s)):
            if s[i] in vow :
                current_vow += 1
            if s[i - k] in vow :
                current_vow -= 1
            max_vow = max(max_vow,current_vow)
        return max_vow                