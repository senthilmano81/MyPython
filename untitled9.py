# New change
import sys
def minSquares(n,dp):
    ''' Return Minimum no of steps required to reach 1 using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n == 1: 
        return 0 
    
    if n in dp: 
        return dp[n]
    
    ans = sys.maxsize 
    for m in range(1,n+1): 
        if m**2 > n: 
            break 
        if (n-m) in dp: 
            ans1 = dp[n-m]
        else: 
            ans1 = minSquares(n-m,dp)
            dp[n-m] = ans1
        ans = min(ans,ans1)
    
    return 1 + ans 

# Main
n=int(input())
dp = {}
print(minSquares(n,dp))
