class Node:
    def __init__(self, key =0 , val = 0):
        self.freq = 1
        self.val = val
        self.key = key
        self.next = None
        self.pre = None

class DoublyLinkedList:
    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.pre = self.left
        self.size = 0

    def remove(self, node):
        n = node.next
        p = node.pre
        p.next = n
        n.pre = p
        self.size -= 1

    def add(self, node):
        p = self.right.pre
        p.next = node
        node.pre = p
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
        #increasefre of node
        #put it in right freq group
        old_freq = node.freq
        self.freq[old_freq].remove(node) # f map stores list node has f and list has size
        if old_freq == self.min_freq and self.freq[old_freq].size == 0:
            self.min_freq += 1

        node.freq += 1
        if node.freq not in self.freq:
            self.freq[node.freq] = DoublyLinkedList()
        self.freq[node.freq].add(node)



    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.update_freq(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.update_freq(node)

        if len(self.cache) == self.cap:
            lfu_list = self.freq[self.min_freq]
            ntr = lfu_list.left.next
            # self.freq[self.min_freq].remove(ntr)
            lfu_list.remove(ntr)
            del self.cache[ntr.key]

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