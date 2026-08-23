class MinStack:

    def __init__(self):
        self.mins  = []
        self.st = []



        

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1])) 



        

    def pop(self) -> None:
        self.st.pop()
        self.mins.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
