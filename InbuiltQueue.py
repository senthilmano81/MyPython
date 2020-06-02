import queue

q = queue.Queue()

q.put(0)
q.put(1)
q.put(2)
q.put(3)
q.put(4)
print(q.queue[0])

print(q.qsize())
while not q.empty(): 
    print(q.get())