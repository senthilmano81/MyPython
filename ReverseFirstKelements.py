
import queue

def reverseFirstK(q,k,i=1):
    if q.qsize() <= 1 or i > k : 
        return
    data = q.get()
    reverseFirstK(q,k,i+1)
    q.put(data)
    if i == 1: 
        n = q.qsize() - k 
        for i in range(n): 
            q.put(q.get())
    return 
        

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
	q.put(ele)
k = int(input())
reverseFirstK(q,k) 
while(q.qsize()>0):
	print(q.get())
	n-=1