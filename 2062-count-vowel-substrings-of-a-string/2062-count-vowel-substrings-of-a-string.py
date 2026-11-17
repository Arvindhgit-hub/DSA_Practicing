class Solution(object):
    def countVowelSubstrings(self, word):
        vow = set("aeiou")
        n = len(word)
        count = 0
        for i in range(n):
            seen = set()
            for j in range(i,n):
                if word[j] not in vow:
                    break
                seen.add(word[j])
                if len(seen) == 5:
                    count += 1    
        return count            