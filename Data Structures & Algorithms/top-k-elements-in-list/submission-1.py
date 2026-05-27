class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        heap = []
        for num, freq in freqs.items():
            heapq.heappush(heap,(freq, num))
        
        return [num for freq,num in heapq.nlargest(k, heap)]
