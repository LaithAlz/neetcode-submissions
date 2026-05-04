class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.prev

        new_node.next = self.tail
        new_node.prev = last_node
        last_node.next = new_node
        
        self.tail.prev = new_node
        
    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        next_node = self.head.next

        new_node.prev = self.head
        new_node.next = next_node
        next_node.prev = new_node
        self.head.next = new_node
        
        

    def pop(self) -> int:
        if (self.isEmpty()):
            return -1
        pop_node = self.tail.prev
        prev_node = pop_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node
        
        return pop_node.value

        

    def popleft(self) -> int:
        if (self.isEmpty()):
            return -1
        
        pop_node = self.head.next
        next_node = pop_node.next

        self.head.next = next_node
        next_node.prev = self.head

        return pop_node.value


        
