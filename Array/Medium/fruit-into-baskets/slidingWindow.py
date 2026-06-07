class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashMap = {}
        i = 0
        maxFruit = 0

        for j in range(len(fruits)):
            hashMap[fruits[j]] = hashMap.get(fruits[j], 0) + 1

            while len(hashMap) > 2:
                hashMap[fruits[i]] -= 1

                if hashMap[fruits[i]] == 0:
                    del hashMap[fruits[i]]

                i += 1

            maxFruit = max(maxFruit, j - i + 1)

        return maxFruit