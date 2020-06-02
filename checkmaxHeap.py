import heapq
def checkMaxHeap(lst,parent=0):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if (parent * 2 + 1) > (len(lst) - 1): 
        return True
    
    child1 = parent * 2 + 1
    if lst[child1]  > lst[parent]: 
        return False 
    
    child2 = parent * 2 + 2 
    if child2 > (len(lst) - 1): 
        return True
    
    if lst[child2] > lst[parent]: 
        return False 
    
    return checkMaxHeap(lst,child1) and checkMaxHeap(lst,child2)

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
