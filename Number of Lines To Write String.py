class Solution(object):
    def numberOfLines(self, widths, s):
        lines = 1
        total_width = 0
        for char in s:
            width = widths[ord(char) - ord('a')]
            if total_width + width > 100:
                lines += 1
                total_width = width
            else:
                total_width += width 
        return [lines, total_width]
