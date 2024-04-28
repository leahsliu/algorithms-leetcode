class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        split_str = list(s)
        for i,char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    # extra close parentheses
                    split_str[i] = ""
        
        # extra open parentheses
        for i in stack:
            split_str[i] = ""
        return "".join(split_str)
            
        
        