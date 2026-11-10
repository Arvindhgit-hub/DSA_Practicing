class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        answer = [0] * n
        prev = -float('inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = i - prev
        prev = float('inf')
        for i in range(n - 1,-1,-1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)
        Iden = answer
        return answer           