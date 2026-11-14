class Node:
    def __init__(self, key=0, val=0, next= None, pre=None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.pre = self.left

    def remove(self, node):
        n = node.next 
        pre = node.pre
        pre.next = n
        n.pre = pre

    def insert(self, node):
        n = self.right.pre
        n.next = node
        node.pre = n
        node.next = self.right
        self.right.pre = node
            

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
          
        node = self.cache.get(key)
        self.remove(node)
        self.insert(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        node = self.cache[key]
        self.insert(node)

        if len(self.cache) > self.cap:
            ntr = self.left.next
            self.remove(ntr)
            del self.cache[ntr.key] 



        




            

        




        
