class Solution(object):
    def customSortString(self, order, s):
        count = Counter(s)
        res = []
        for char in order:
            if char in count:
                res.append(char * count[char])
                del count[char]
        for char, freq in count.items():
            res.append(char * freq)        
        return "".join(res)    