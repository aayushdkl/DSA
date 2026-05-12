class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            sumOfSqOfDig=0
            while(n>0):
                s = n%10
                n=n//10
                sumOfSqOfDig += s*s
            return sumOfSqOfDig

        slow = getNext(n)
        fast = getNext(getNext(n))
        while fast!= 1 and slow!=fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
        return fast == 1