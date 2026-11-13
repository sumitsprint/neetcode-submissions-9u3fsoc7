class TimeMap:

    def __init__(self):
        self.s = {}



        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.s:
            self.s[key] = []
        
        self.s[key].append((timestamp, value))
                
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.s:
            return ""

        else:
            left = 0
            right = len(self.s.get(key)) - 1

            while left <= right:
                mid = (left + right) // 2
                if self.s.get(key)[mid][0] > timestamp:
                    right = mid - 1

                else:
                    left = mid + 1
            if right < 0:
                return ""        

            return self.s.get(key)[right][1]            





            
        
