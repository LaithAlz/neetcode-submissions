class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.queue = []

    def get(self, key: int) -> int:
        if key in self.map:
            print("queue after eviction", self.queue, self.map)
            self.queue.remove(key)
            self.queue.append(key)
            return self.map[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        print(self.map)
        print(self.queue)
        if key in self.map:
            self.map[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        else:
            if len(self.queue) >= self.capacity:
                popped = self.queue.pop(0)
                print("queu after eviction", self.queue, self.map)
                self.map.pop(popped, None)
                self.map[key] = value
                self.queue.append(key)
            else:
                self.queue.append(key)
                self.map[key] = value
