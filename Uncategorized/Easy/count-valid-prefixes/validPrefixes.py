class Solution:
    def countValidPrefixes(self, s: str) -> int:
        c0 = 0
        c1 = 0
        ans = 0
        for char in s:
            if char == '0':
                c0 += 1
            else:
                c1 += 1
            if abs(c0 - c1) <= 1:
                ans += 1
        return ans