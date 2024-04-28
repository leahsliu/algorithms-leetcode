class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        currSum = 0
        diffs = {0:1}
        for num in nums:
            currSum += num
            diff = currSum - k
            diffs[currSum] = 1 + diffs.get(currSum, 0)
            print("diff ", diff)
            print("diffs ", diffs)
            res += diffs.get(diff, 0)




        return res














s1 = Solution()
print(s1.subarraySum([1,2,3], 2))


        # currSum = 0
        # res = 0
        # prefixSums = {0:1}

        # for num in nums:
        #     currSum += num
        #     difference = currSum - k

        #     res += prefixSums.get(difference, 0)
        #     prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
        # return res