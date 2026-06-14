class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        min_dist = 1000000
        last_popped_dist = 1000000
        i = 0
        while i < len(points):
            x= points[i][0]
            y= points[i][1]
            dist = math.sqrt(x ** 2 + y **2)
            heapq.heappush(heap, (dist, [x,y]))

            i += 1
        print(heap)
        res = []
        counter = 0
        while counter < k:
            dist, points=heapq.heappop(heap)
            res.append(points)
            counter += 1
        return res
