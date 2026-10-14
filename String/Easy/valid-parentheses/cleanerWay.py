class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for ch  in s:
            if ch == "(":
                stack.append(")")
            elif ch == "{":
                stack.append("}")
            elif ch == "[":
                stack.append("]")
            elif not stack or not ch== stack[-1]:
                return False
            else:
                stack.pop()                        
        return not stack