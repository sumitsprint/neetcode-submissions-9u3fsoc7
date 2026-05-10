class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
        
    def hash_(self, key):
        if isinstance(key, int):
            return key % self.size
        if isinstance(key, str):
            return sum(ord(c) for c in key) % self.size        
        

    def put(self, key: int, value: int) -> None:
        index = self.hash_(key)
        for i, (k,v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return 
        self.buckets[index].append((key, value))
        return
        
                
                



        

    def get(self, key: int) -> int:
        index = self.hash_(key)
        for i, (k,v) in enumerate(self.buckets[index]):
            if k == key:
                return v
        return -1        
        # self.buckets[index].append((key, value))

        

    def remove(self, key: int) -> None:
        index = self.hash_(key)
        for i, (k,v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index].pop(i)
                return
                
        # return -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)