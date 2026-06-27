class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cacheHash = {}
        self.capacity = capacity
        
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cacheHash:
            return -1
        
        new_tail = self.cacheHash[key]
        new_tail.prev.next = new_tail.next 
        new_tail.next.prev = new_tail.prev
        
        last = self.tail.prev
        last.next = new_tail
        new_tail.prev = last

        new_tail.next = self.tail
        self.tail.prev = new_tail 

        return new_tail.value

    def put(self, key: int, value: int) -> None:
        if key in self.cacheHash:
            new_tail = self.cacheHash[key]
            new_tail.prev.next = new_tail.next 
            new_tail.next.prev = new_tail.prev
            
            last = self.tail.prev
            last.next = new_tail
            new_tail.prev = last

            new_tail.next = self.tail
            self.tail.prev = new_tail 

            new_tail.value = (value)
            self.cacheHash[key] = new_tail
        
        else:
            if self.capacity == len(self.cacheHash):
                first = self.head.next
                first.next.prev = first.prev
                first.prev.next = first.next
                del self.cacheHash[first.key]
                first.next = None
                first.prev = None

            last = self.tail.prev
            last.next = Node(key, value)
            self.cacheHash[key] = last.next

            last.next.prev = last 
            last.next.next = self.tail
            self.tail.prev = last.next