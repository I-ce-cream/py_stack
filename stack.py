# class Stack():
#     def __init__(self):
#         self.stack = []
#
#     def size(self):
#         return len(self.stack)
#
#     def is_empty(self):
#         return self.size() == 0
#
#     def push(self,data):
#         self.stack.append(data)
#
#     def pop(self):
#         if self.is_empty():
#             return None
#         else:
#             return self.stack.pop()
#
#     def top(self):
#         if self.is_empty():
#             return None
#         else:
#             return self.stack[-1]
#
#     def prtStack(self):
#         print(self.stack)
#
#     def clean(self):
#         del self.stack[:]
#
#
#
#
# s = Stack()
#
# s.push(1)
# s.push(2)
# s.push(3)
# s.prtStack()
# s.clean()
# s.size()
#
# #
# # s.prtStack()
# # s.pop()
# # s.prtStack()
# #
# # print(s.is_empty())
#
#
# # pro = dict(zip('+-*/', '1122'))
# # print(pro)
# # myStack = Stack()
# #
# # for i in range(6):
# #     myStack.push(i)
# #
# # myStack.prtStack()
# # myStack.top()
# #
# # for i in range(8):
# #     myStack.pop()
# #
# # myStack.prtStack()