class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        doubled_s = s + s
        if goal in doubled_s:
            return True
        return False       
