class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans = []

        def dfs(idx, prev_one, cost, curr):
            if idx == n:
                ans.append("".join(curr))
                return

            curr.append('0')
            dfs(idx + 1, False, cost, curr)
            curr.pop()

            if not prev_one and cost + idx <= k:
                curr.append('1')
                dfs(idx + 1, True, cost + idx, curr)
                curr.pop()

        dfs(0, False, 0, [])
        return ans