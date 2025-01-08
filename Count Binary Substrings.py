class Solution(object):
    def countBinarySubstrings(self, s):
        groups = []
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)  
        count_binary_substrings = 0
        for i in range(1, len(groups)):
            count_binary_substrings += min(groups[i - 1], groups[i])
        return count_binary_substrings
