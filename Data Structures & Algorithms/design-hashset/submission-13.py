class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def hash_(self, key):
        if isinstance(key, str):
            return sum(ord(c) for c in key) % self.size
        if isinstance(key, int):
            return key % self.size        
        

    def add(self, key: int) -> None:
        index = self.hash_(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)
            return

    # def hash_(self, key):
    #     if isinstance(key, str):
    #         return sum(ord(c) for c in key) % self.size       
        

    def remove(self, key: int) -> None:
        index = self.hash_(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

        

    def contains(self, key: int) -> bool:
        index = self.hash_(key)
        return key in self.buckets[index]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)