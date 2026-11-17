class Node:
    def __init__(self, key=0, val=0):
        self.next = None
        self.pre = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.pre = self.left


    def remove(self, node):
        pre = node.pre
        n = node.next
        pre.next = n
        n.pre = pre

    def add(self, node):
        pre = self.right.pre 
        pre.next = node
        node.pre = pre
        node.next = self.right
        self.right.pre = node     
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            del self.cache[key]
            
        node = Node(key, value)
        self.cache[key] = node
        self.add(node)
        if len(self.cache) > self.cap:
            ntr = self.left.next
            self.remove(ntr)
            del self.cache[ntr.key]    
        
