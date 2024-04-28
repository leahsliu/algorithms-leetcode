class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parenMap = {"}":"{", "]":"[", ")":"("}

        for bracket in s:
            if bracket in parenMap:
                if stack and stack[-1] == parenMap[bracket]:
                    stack.pop()
                elif stack and stack[-1] != parenMap[bracket]:
                    return False
            else:
                stack.append(bracket)
        

        return True if not stack else False


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("()[]{]"))























        # pMap = {"}":"{", ")":"(", "]":"["}

        # stack = []
        # for i in range(len(s)):
        #     # check ending bracket in map
        #     if stack and s[i] in pMap:
        #         if pMap[s[i]] != stack[-1]:
        #             return False
        #         else:
        #             stack.pop()
        #     else:
        #         stack.append(s[i])





        # return True if not stack else False