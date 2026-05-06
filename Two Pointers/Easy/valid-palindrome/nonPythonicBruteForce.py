class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        reversedRes=""
        for ch in s:
            if ch.isalnum():
                res+=ch.lower()   
        for ch in res:
            reversedRes = ch+reversedRes         
        return res == reversedRes