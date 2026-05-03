class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for i in range(self.size)]

    def _hash(self, key):
        if isinstance(key, str):
            return sum(ord(c) for c in key) % self.size
        elif isinstance(key, int):
            return key % self.size            

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        for i, (k,v) in enumerate(self.buckets[index]):
            if key == k:
                self.buckets[index][i] = (key, value)
                return

        self.buckets[index].append((key,value))
        return

        

    def get(self, key: int) -> int:
        index = self._hash(key)
        for i, (k,v) in enumerate(self.buckets[index]):
            if key == k:
                return v
        return -1    
                

        
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        for i, (k,v) in enumerate(self.buckets[index]):
            if key == k:
                self.buckets[index].pop(i)
                return
                  

        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)