class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        freq = {}
        i = 0
        maxLen = 0

        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1

            while len(freq) > k:
                freq[s[i]] -= 1

                if freq[s[i]] == 0:
                    del freq[s[i]]

                i += 1

            maxLen = max(maxLen, j - i + 1)

        return maxLen