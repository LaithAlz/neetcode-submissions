class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        print(intervals)

        results = []
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            if len(results) > 0:
                last_interval = results[-1]
                last_interval_start = last_interval[0]
                last_interval_end = last_interval[1]

                if start <= last_interval_end:
                    last_interval[1] = max(last_interval_end, end)
                else: 
                    results.append([start, end])
            else:
                results.append([start, end])
        return results