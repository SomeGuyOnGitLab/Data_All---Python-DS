class Solution(object):
    def rotateString(self, s, goal):
        for i in range(len(s)):
            s = s[1:]+s[:1]
            if s == goal:
                return True
        return False
