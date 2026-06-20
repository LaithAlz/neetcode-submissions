class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # heap = [-x for x in nums]
        heap = nums[::]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return heap[0]