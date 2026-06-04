class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 1):
            counter = 0
            curr_temp = temperatures[i]
            j = i + 1
            while j < len(temperatures):
                new_temp = temperatures[j]
                print("curr_temp", curr_temp)
                print("new_temp", new_temp)
                counter += 1
                if curr_temp < new_temp:
                    print("found warmer day")
                    res[i] = counter
                    break
                print("did not find warmer day")
                j += 1
            print("counter", counter)
            print(f"setting position {i} to {counter}")
            print("")
        return res
            