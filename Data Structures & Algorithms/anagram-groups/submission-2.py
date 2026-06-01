class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            counts = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                counts[index] += 1
            print(counts)
            counts = tuple(counts)
            if(counts not in groups):
                groups[counts] = [word]
            else:
                groups[counts].append(word)
        return [value for key, value in groups.items()]

