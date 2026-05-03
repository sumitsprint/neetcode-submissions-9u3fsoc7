class MyHashMap:

    def __init__(self):
        self.size = 5
        self.buckets = [[] for i in range(self.size)]
        

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))        
        

    def get(self, key: int) -> int:
        index = key % self.size
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return v
        return -1        
        

    def remove(self, key: int) -> None:
        index = key % self.size
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)