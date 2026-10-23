# how the individual node will look like

        
class LRUCache:
    
# initialised boundary nodes of linked list and dictionary for easy retreival
    def __init__(self, capacity: int):
        self.cap = capacity  #attributes that other methods can use
        self.cache = {} # dictionary
        self.left = Node() # Least recently used side, dummy node
        self.right = Node()  # Most recently used side, dummy node
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
    # implement the LRU Cache behaviour

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
           
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


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None
#When you write self.variable, you're storing that variable as an attribute of the object. Other methods belonging to that object can access it through self


        
