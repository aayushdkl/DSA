class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        max_range = -1
        ans = 0

        for num in nums:
            x = num
            mn = 9
            mx = 0
            while x:
                d = x % 10
                mn = min(mn, d)
                mx = max(mx, d)
                x //= 10
            r = mx - mn
            if r > max_range:
                max_range = r
                ans = num
            elif r == max_range:
                ans += num

        return ans