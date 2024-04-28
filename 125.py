
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            elif not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1

        return True

print("valid palindrome q: ")
s1 = Solution()
print(s1.isPalindrome("racecar"))
print(s1.isPalindrome("A man, a plan, a canal: Panama"))
print(s1.isPalindrome("A man, a plan, a d"))
print(s1.isPalindrome(" "))



        # new = ''
        # for a in s:
        #     if a.isalpha() or a.isdigit():
        #         new += a.lower()
        # return (new == new[::-1])




















        # start = 0
        # end = len(s) - 1

        # while start < end:
        #     if not s[start].isalnum():
        #         start+=1
        #     elif not s[end].isalnum():
        #         end -= 1
        #     elif s[start].isalnum() and s[end].isalnum() and s[start].lower() == s[end].lower():
        #         print("start",s[start].lower())
        #         print("end", s[end].lower())
        #         start += 1
        #         end -= 1
        #     else:
        #         return False
        
        # return True