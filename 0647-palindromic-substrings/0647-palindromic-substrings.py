class Solution(object):
    def countSubstrings(self, s):
        count = 0
        n = len(s)
        for i in range(n):
            count += self.expandAroundCenter(s,i,i)
            count += self.expandAroundCenter(s,i,i+1)
        return count 
    def expandAroundCenter(self,s,left,right):
        sub_count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            sub_count += 1
            left -= 1
            right += 1 
        return sub_count          