class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        self.stack.append(x)
        if len(self.minStack) and x == self.minStack[-1][0]:
            self.minStack[-1] = (x, self.minStack[-1][1] + 1)





