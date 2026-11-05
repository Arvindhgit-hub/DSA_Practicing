class Solution(object):
    def isPalindrome(self, s):
        filtered = ""
        for char in s:
            if char.isalnum():
                filtered += char.lower()
        left = 0
        right = len(filtered) - 1
        for i in range(len(filtered)//2):
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        return True                