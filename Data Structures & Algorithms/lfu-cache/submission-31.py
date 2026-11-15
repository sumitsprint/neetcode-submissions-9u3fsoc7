class Node:
    def __init__(self, key=0, val=0):
        self.freq = 1
        self.next = None
        self.pre = None
        self.key = key
        self.val = val

class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.pre = self.left

    def remove(self, node):
        pre = node.pre
        n = node.next
        pre.next = n
        n.pre = pre
        self.size -= 1
    
    def add(self, node):
        pre = self.right.pre
        pre.next = node
        node.pre = pre
        node.next = self.right
        self.right.pre = node
        self.size += 1 
    
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.freq = {}
        self.min_freq = 0 

    def update_freq(self, node):
        old_freq = node.freq
        self.freq[old_freq].remove(node)
        if old_freq == self.min_freq and self.freq[self.min_freq].size == 0:
            self.min_freq += 1

        node.freq += 1
        if node.freq not in self.freq:
            self.freq[node.freq] = DoublyLinkedList()

        self.freq[node.freq].add(node)
            
            




    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
            
        node = self.cache.get(key)
        self.update_freq(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache.get(key)
            node.val = value
            self.update_freq(node)
            return
        if len(self.cache) == self.cap:
            lfu = self.freq[self.min_freq].left.next
            self.freq[self.min_freq].remove(lfu)
            del self.cache[lfu.key]

            
                

        node = Node(key, value)
        self.cache[key] = node
        if 1 not in self.freq:
            self.freq[1] = DoublyLinkedList()
        self.freq[1].add(node)
        self.min_freq = 1
                
            
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)