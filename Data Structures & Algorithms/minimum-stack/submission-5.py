class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:    

            self.minstack.append(min(val, self.minstack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

        
        #When you use your MinStack, the user of the class still has one object:
#The key is that minstack is not storing the minimum elements themselves. It stores the minimum-so-far corresponding to each position in the main stack.
#stack:     [5, 4, 6, 5]
#minstack:  [5, 4, 4, 4]