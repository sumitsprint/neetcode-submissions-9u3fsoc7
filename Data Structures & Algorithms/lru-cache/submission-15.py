# how the individual node will look like
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None
        
class LRUCache:
    
#  initialised boundary nodes of linked list and dictionary for easy retreival
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.pre = self.left

# remove and insert implemented operations in it    
    def remove(self, node):
        n = node.next
        pre = node.pre
        pre.next = n
        n.pre = pre

    def add(self, node):
        pre = self.right.pre
        pre.next = node
        node.next = self.right
        self.right.pre = node
        node.pre = pre
    
    # maintaining lru cache

    def get(self, key: int) -> int:
        if key not in self.cache:
            return - 1
           
        node = self.cache[key]   
        self.remove(node)
        self.add(node)
        return node.val

    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        node = self.cache[key]
        self.add(node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



        
