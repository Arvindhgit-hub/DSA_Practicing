class Solution(object):
    def findAnagrams(self, s, p):
        ns = len(s)
        np = len(p)
        if ns < np:
            return []
        pcount = [0] * 26
        scount = [0] * 26
        for i in range(np):
            pcount[ord(p[i]) - ord('a')] += 1
            scount[ord(s[i]) - ord('a')] += 1
        result = []
        if pcount == scount:
            result.append(0)
        for i in range(np,ns):
            scount[ord(s[i]) - ord('a')] += 1
            scount[ord(s[i - np]) - ord('a')] -= 1
            if pcount == scount:
                result.append(i - np + 1)
        return result                   