class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        boatCount = 0
        left = 0
        right = n-1
        people.sort()
        while(left<=right):
            sum = people[left]+people[right]
            if sum<=limit:
                left+=1
            boatCount+=1
            right-=1
        return boatCount