import heapq
def kLargest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    arr = lst[:k]
    heapq.heapify(arr)
    for ele in lst[k:]:
        if ele > arr[0]: 
            heapq.heapreplace(arr,ele)
    return arr 
# Main
# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')
