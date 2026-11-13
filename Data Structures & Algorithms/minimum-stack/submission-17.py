class MinStack:

    def __init__(self):
        self.minst = []
        self.st = []

        

    def push(self, val: int) -> None:
        
        self.st.append(val)
        if not self.minst:
            self.minst.append(val)
        else:
            self.minst.append(min(self.minst[-1], val))    
        
        

    def pop(self) -> None:
        if self.st:
            self.st.pop()
            self.minst.pop()

        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.minst[-1]
        
