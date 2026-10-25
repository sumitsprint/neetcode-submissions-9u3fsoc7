class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None
        self.freq = 1

class doublyLinkedList:
    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.pre = self.left
        self.size = 0 #size tracks how many real nodes the list contains

    def remove(self, node):
        n = node.next
        pre = node.pre
        pre.next = n
        n.pre = pre
        
        self.size -= 1 

    def add(self, node):
        pre = self.right.pre
        pre.next = node
        node.next = self.right
        self.right.pre = node
        node.pre = pre
        self.size += 1

        
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.freq = {}
        self.min_freq = 0 # self.min_freq: tracks the smallest frequency currently present in the cache.

        # This method moves an existing node from its current frequency list to the next one
    def update_freq(self, node):
        old_freq = node.freq
        self.freq[old_freq].remove(node)
        # if old fre has become empty
        if old_freq== self.min_freq and self.freq[old_freq].size == 0:
            self.min_freq += 1

        node.freq += 1
        if node.freq not in self.freq:
            self.freq[node.freq] = doublyLinkedList()
        self.freq[node.freq].add(node)  


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.update_freq(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        # if self.cap == 0:
            # return

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.update_freq(node) # preserve the freq
            return 

        if len(self.cache) == self.cap:
            lfu_list = self.freq[self.min_freq]
            node_to_remove = lfu_list.left.next
            lfu_list.remove(node_to_remove)
            del self.cache[node_to_remove.key]

        node = Node(key, value)
        self.cache[key] = node 
        if 1 not in self.freq:
            self.freq[1] = doublyLinkedList()

        self.freq[1].add(node)
        self.min_freq = 1           
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)