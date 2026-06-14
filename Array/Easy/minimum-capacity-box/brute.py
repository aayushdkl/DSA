class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        best_capacity = float("inf")
        answer = -1

        for i in range(len(capacity)):
            if capacity[i] >= itemSize and capacity[i] < best_capacity:
                best_capacity = capacity[i]
                answer = i

        return answer