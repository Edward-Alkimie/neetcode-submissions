class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True 
        stack = []
        for bracket in s:
            if bracket == "{":
                stack.append(bracket)
            elif bracket == "(":
                stack.append(bracket)
            elif bracket == "[":
                stack.append(bracket)
            elif (bracket == "]") & (len(stack) > 0) :
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif (bracket == ")") & (len(stack) > 0):
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif (bracket == "}") & (len(stack) > 0):
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        if len(stack) != 0:
            return False
        
        return True  



        