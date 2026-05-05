class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        boatCount = 0
        left = 0
        right = n-1
        people.sort()
        while(left<=right):
            if left!=right:
                sum = people[left]+people[right]
                if sum<=limit:
                    boatCount+=1
                    left+=1
                    right-=1
                else:
                    boatCount+=1
                    right-=1
            else:
                boatCount+=1
                left+=1
                right-=1    
        return boatCount