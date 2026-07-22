class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.minn) == 0 or val < self.minn[-1]):
            self.minn.append(val)
        else:
            self.minn.append(self.minn[-1])

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.minn = self.minn[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn[-1]
