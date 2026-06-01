class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            word_sorted = "".join(sorted(word))
            print(word_sorted)
            
            if word_sorted not in groups:
                groups[word_sorted] = [word]
            else:
                groups[word_sorted].append(word)
        
        return [value for key, value in groups.items()]