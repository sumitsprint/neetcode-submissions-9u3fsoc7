class Node:
    def __init__(self, key=0, val=0 ):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node() #dummy Node
        self.right = Node() #dummy node
        self.left.next = self.right
        self.right.pre = self.left
        self.cache = {}

    def remove(self, node):
        pre = node.pre 
        n = node.next
        pre.next = n
        n.pre = pre

    def insert(self, node):
        pre = self.right.pre
        pre.next = node
        node.pre = pre
        node.next = self.right
        self.right.pre = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]    
        self.remove(node) # remove
        self.insert(node) # insert in front
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node    
        
        self.insert(node)

        if len(self.cache) > self.cap:
            # self.remove(self.left.next)
            # del self.cache[self.left.next.key]
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


