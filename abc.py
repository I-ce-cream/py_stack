class Stack():
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None  #("stack is empty")
        else:
            return self.stack.pop()

    def top(self):
        if self.is_empty():
            return None  #("stack is empty")
        else:
            return self.stack[-1]

    def prtStack(self):
        print(self.stack)

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def clean(self):
        del self.stack[:]




# s = Stack()
# s.top()
# s.push(1)
# s.push(2)
#
# s.prtStack()
# s.pop()
# s.prtStack()
#
# print(s.is_empty())
