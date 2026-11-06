class Solution(object):
    def longestPalindrome(self, s):
        from collections import Counter
        count = Counter(s)
        length = 0
        has_odd = False
        for freq in count.values():
            length += freq // 2 * 2
            if freq % 2 != 0:
                has_odd = True
        if has_odd:
            length += 1
        return length            