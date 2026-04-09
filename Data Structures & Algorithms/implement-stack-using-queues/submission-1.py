class MyStack:

    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
        n = len(self.q1)
        while n>1:
            self.q1.append(self.q1.popleft())
            n-=1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return True if not self.q1 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()