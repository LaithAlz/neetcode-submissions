class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            largest_stone = -1 * heapq.heappop(heap)
            second_largest_stone = -1 * heapq.heappop(heap)

            if largest_stone == second_largest_stone:
                continue
            elif largest_stone > second_largest_stone:
                val = largest_stone - second_largest_stone
                heapq.heappush(heap, -val)
        
        if len(heap) == 1:
            return -1 * heap[0]
        else:
            return 0