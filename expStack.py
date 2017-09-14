# -*- coding:utf-8 -*-
# from pythonds.basic.stack import Stack

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)



s = Stack()

print(s.isEmpty())
s.push(4)
s.push('cat')
print(s.size())