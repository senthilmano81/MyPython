import heapq
def kthLargest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    heapq._heapify_max(lst)
    for i in range(k): 
        ans = heapq._heappop_max(lst)
    return ans 
    
# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)
