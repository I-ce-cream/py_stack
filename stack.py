class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            print("stack is empty")
        else:
            return self.stack.pop()

    def prtStack(self):
        print(self.stack)

    def top(self):
        return self.stack[-1]

# pro = dict(zip('+-*/', '1122'))
# print(pro)
# myStack = Stack()
#
# for i in range(6):
#     myStack.push(i)
#
# myStack.prtStack()
# myStack.top()
#
# for i in range(8):
#     myStack.pop()
#
# myStack.prtStack()