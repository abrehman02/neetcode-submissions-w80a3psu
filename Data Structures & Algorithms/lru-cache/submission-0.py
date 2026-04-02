class Node:

    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # capacity 
        self.cap = capacity 

        # creating dummy nodes
        self.left = Node(0,0)
        self.right = Node(0,0)

        # linking the dummy head and tail
        self.left.next = self.right
        self.right.prev = self.left

        # cache hashmap for O(1) retreival
        self.cache = {}        

    def insert(self, node):
        # remove the tail here link head to node current
        self.right.prev.next = node
        node.prev = self.right.prev

        node.next = self.right
        self.right.prev = node

    def remove(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache :
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # node = Node([key, value])
        if key in self.cache:
            # insert this in cache
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # update the value if its in already
        if len(self.cache) > self.cap :
            # delete LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
