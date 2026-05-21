class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1

        for num, freq in freqs.items():
            heapq.heappush(heap, (freq, num))
        
        return [num[1] for num in heapq.nlargest(k, heap)]
