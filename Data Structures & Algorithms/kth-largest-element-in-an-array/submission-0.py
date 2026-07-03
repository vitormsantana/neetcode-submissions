import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.k = k
        heapq.heapify(nums)
        while len(nums) > self.k:
            heapq.heappop(nums)
        return nums[0]