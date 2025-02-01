import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for elem in nums:
            heapq.heappush(min_heap, elem)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]
                


