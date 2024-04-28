class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        numSet = set(nums)
        for num in numSet:
            # if statement is true when num is 
            # smallest number of a consecutive sequence
            if num-1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                maxLen = max(maxLen, length)

        return maxLen
    
s = Solution()
print(s.longestConsecutive([3,100,2,200,1,4]))