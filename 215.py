import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]


s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))

        # maxHeap = [-num for num in nums]
        # heapq.heapify(maxHeap)

        # for i in range(k-1):
        #     heapq.heappop(maxHeap)
        
        # return -1*maxHeap[0]





        # minHeap = nums[:]
        # heapq.heapify(minHeap)

        # while len(minHeap) > k:
        #     heapq.heappop(minHeap)
        # return minHeap[0]