class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, x):
        self.stack.append(x)
        if self.mins != []:
            if self.mins[-1] > x:
                self.mins.append(x)
            else:
                self.mins.append(self.mins[-1])
        else:
            self.mins.append(x)

    def pop(self):
        self.stack.pop()
        self.mins.pop()

    def top(self):
        if self.stack != []:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        if self.mins != []:
            return self.mins[-1]
        else:
            return None

if __name__ == '__main__':
    m = MinStack()
    m.push(-2)
    m.push(0)
    m.push(-3)
    assert m.getMin() == -3
