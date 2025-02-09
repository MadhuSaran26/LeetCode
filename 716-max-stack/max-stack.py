class MaxStack:

    def __init__(self):
        # self.stack -> max heap to keep track of top
        # self.values -> max heap to keep track of max value
        # self.cnt -> total count in stack
        # self.remove_set -> hash set to keep track of deleted items
        self.stack = []
        self.values = []
        self.cnt = 0
        self.remove_set = set()

    def push(self, x: int) -> None:
        # pushes the value into stack
        self.stack.append((-self.cnt, -x))
        heappush(self.values, (-x, -self.cnt))
        self.cnt += 1

    def pop(self) -> int:
        # removes top of stack
        while self.stack and self.stack[-1][0] in self.remove_set:
            self.stack.pop()
        idx, value = self.stack.pop()
        self.remove_set.add(idx)
        return -value

    def top(self) -> int:
        # returns top of stack
        while self.stack and self.stack[-1][0] in self.remove_set:
            self.stack.pop()
        return -self.stack[-1][1]      

    def peekMax(self) -> int:
        # returns max value in stack
        while self.values and self.values[0][1] in self.remove_set:
            heappop(self.values)
        return -self.values[0][0]      

    def popMax(self) -> int:
        # removes max value from stack
        while self.values and self.values[0][1] in self.remove_set:
            heappop(self.values)
        value, idx = heappop(self.values)
        self.remove_set.add(idx)
        return -value


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()