class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs1 = Counter(s1)

        l = 0
        for r in range(len(s1), len(s2) + 1):
            print(s2[l:r])
            freqs2 = Counter(s2[l:r])
            print(freqs1, freqs2)
            if freqs2 != freqs1:
                l += 1
            if freqs2 == freqs1:
                return True
        
        return False