import sys
def minSquares(n,dp):
    ''' Return Minimum no of steps required to reach 1 using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n == 0: 
        return 0 
    
    if n == 1: 
        return 1
    
    if n in dp: 
        return dp[n]
    
    ans = sys.maxsize 
    for m in range(1,n+1): 
        k = m**2 
        if k > n: 
            break
        if (n-k) in dp: 
            ans1 = dp[n-k]
        else: 
            ans1 = minSquares(n-k,dp)
            dp[n-k] = ans1
        ans = min(ans,ans1)
    
    return 1 + ans 

# Main
n=int(input())
dp = {}
print(minSquares(n,dp))
