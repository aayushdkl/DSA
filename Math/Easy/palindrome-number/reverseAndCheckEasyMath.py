class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x == 0:
            return True
        if x%10 == 0:
            return False
        if x == 0:
            return True

        origNo = x
        revNo =0
        while x>0:
            lastDig = x%10
            revNo = revNo * 10 + lastDig
            x = x//10
        return revNo == origNo