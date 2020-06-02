import heapq

n = int(input())
arr = [int(x) for x in input().split()]
uidx = int(input())

you  = arr[uidx]
heapq._heapify_max(arr)
time = 0  
out = -9999999
while out < you:
    out = heapq._heappop_max(arr)
    print(out)
    time = time + 1
print(time)