# -*- coding:utf-8 -*-

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)


q = Queue()
q.enqueue('ad')
q.enqueue(8.4)
q.size()
q.isEmpty()

'''
def hotPotato(namelist, num):
	namequeue = Queue()
	for name in namelist:
		namequeue.enqueue(name)
	
	while(namequeue.size()) > 1:
		for i in range(num):
			namequeue.enqueue(namequeue.dequeue())
		
		namequeue.dequeue()

	return namequeue.dequeue()


print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
'''

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],4))

