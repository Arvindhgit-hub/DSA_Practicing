class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word,p):
            m1,m2 = {},{}
            for w_char , p_char in zip(word,p):
                if w_char in m1 and m1[w_char] != p_char:
                    return False
                if p_char in m2 and m2[p_char] != w_char:
                    return False    
                m1[w_char] = p_char
                m2[p_char] = w_char
            return True
        return [word for word in words if match(word , pattern)]    