class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        parent = list(range(26))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            # Always keep the lexicographically smaller character as the root
            if root_x < root_y:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))
        result = []
        for ch in baseStr:
            root = find(ord(ch) - ord('a'))
            result.append(chr(root + ord('a')))
        return "".join(result)