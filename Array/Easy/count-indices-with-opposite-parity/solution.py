class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        even = odd = 0

        for i in range(n - 1, -1, -1):
            if nums[i] % 2:
                ans[i] = even
                odd += 1
            else:
                ans[i] = odd
                even += 1

        return ans