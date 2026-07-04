class RandomizedSet:

    def __init__(self):
        self.elements = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.elements)
        self.elements.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            last_element = self.elements[-1]
            index = self.map[val]
            self.map[val], self.map[self.elements[-1]]= self.map[self.elements[-1]], self.map[val]
            self.elements[-1], self.elements[index] = self.elements[index], self.elements[-1]

            self.elements.pop()
            self.map.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.elements)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()