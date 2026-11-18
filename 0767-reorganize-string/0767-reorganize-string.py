class Solution(object):
    def reorganizeString(self, s):
        count = Counter(s)
        max_heap = [(-freq,char) for char, freq in count.items()]
        heapq.heapify(max_heap)
        res = []
        prev_freq, prev_char = 0,''
        while max_heap:
            freq,char = heapq.heappop(max_heap)
            res.append(char)
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq,prev_char))
            prev_freq,prev_char = freq + 1,char
        result_str = "".join(res)
        return result_str if len(result_str) == len(s) else ""                