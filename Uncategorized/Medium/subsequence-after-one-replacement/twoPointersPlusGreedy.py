class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        used = False

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            elif not used:
                used = True
                i += 1
                j += 1
            else:
                j += 1

        return i == len(s)