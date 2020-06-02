import heapq
def kSmallest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    arr = lst[:k]
    heapq._heapify_max(arr)
    for ele in lst[k:]:
        if ele < arr[0]: 
            heapq._heapreplace_max(arr,ele)
    return arr 
# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
print(*ans)
