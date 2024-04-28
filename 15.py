class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            total = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < len(nums) and left < right:
                if total + nums[left] + nums[right] > 0:
                    right -= 1
                elif total + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    res.append([total, nums[left], nums[right]])
                    break

        return res

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))

print(s.threeSum([0,1,1]))

print(s.threeSum([0,0,0]))