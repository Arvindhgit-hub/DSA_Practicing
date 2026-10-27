class Solution(object):
    def reverse(self, x):
        int_min = -2147483648
        int_max = 2147483647
        
        sign = -1 if x < 0 else 1
        rev_str = str(abs(x))[::-1]
        rev = int(rev_str)*sign
        
        if rev < int_min or rev > int_max:
            return 0

        return rev    


