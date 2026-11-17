class Solution(object):
    def sumPrefixScores(self, words):
        trie = {}
        
        for word in words:
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = {"#": 0}
                curr = curr[char]
                curr["#"] += 1
                
        out = []
        for word in words:
            curr = trie
            score = 0
            for char in word:
                curr = curr[char]
                score += curr["#"]
            out.append(score)
            
        return out