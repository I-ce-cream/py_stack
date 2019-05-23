class Stack():
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def prtStack(self):
        print(self.stack)

    def clear(self):
        del self.stack[:]
		#self.stack = []

#    def min(self):

            


s = Stack()
s.push(1)
s.push(2)
s.prtStack()
print(s.size())

print(s.size())

s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.prtStack()
s.clear()
s.prtStack()
print(s.size())



##  PB  JavaScript   C# 堆栈，  判断括号，  逆波兰表达式/计算，  big O(1)栈内最小值