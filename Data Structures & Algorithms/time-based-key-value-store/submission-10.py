class TimeMap:

    def __init__(self):
        self.store= {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))    
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        left = 0
        arr = self.store[key]
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid+1
        if right < 0: # it emerges naturally if there is no valid timestamp
        # can there be 0 valid candidates?
            return ""         

        return arr[right][1]            







        
