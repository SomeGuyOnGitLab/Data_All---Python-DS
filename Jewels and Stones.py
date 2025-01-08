class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for jewel in jewels:
            count+=stones.count(jewel)
        return count
        
