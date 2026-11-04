class Solution(object):
    def commonChars(self, words):
        min_freq = [float('inf')] * 26
        for word in words:
            current_freq = [0] * 26
            for char in word:
                current_freq[ord(char)-ord('a')] += 1
            for i in range(26):
                min_freq[i] = min(min_freq[i],current_freq[i])
        result = []
        for i in range(26):
            if min_freq[i] > 0 and min_freq[i] != float('inf'):
                result.extend([chr(i + ord('a'))] * min_freq[i])
        return result                    